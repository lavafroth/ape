import inspect
from dataclasses import is_dataclass


class IndividualVariantMethodError(Exception):
    def __init__(self, variant_name, extra_declared_functions):
        message = f"Functions must not be declared on individual enum variants, found functions declared on variant {variant_name}: {', '.join(extra_declared_functions)}."
        super().__init__(message)


class VariantNotDataclassError(Exception):
    def __init__(self, variant_name):
        message = f"AlgebraicEnum variants are required to be dataclasses. Consider adding the `@dataclass` decorator to variant `{variant_name}`."
        super().__init__(message)


def AlgebraicEnum(enum_base):
    for variant_name, variant in enum_base.__dict__.items():
        if not isinstance(variant, type):
            continue
        if not is_dataclass(variant):
            raise VariantNotDataclassError(variant_name)

        extra_declared_functions = {
            function_name
            for function_name, _fn in inspect.getmembers(
                variant, predicate=inspect.isfunction
            )
        } - {
            "__init__",
            "__repr__",
            "__eq__",
            "__replace__",
        }

        if extra_declared_functions:
            raise IndividualVariantMethodError(variant_name, extra_declared_functions)
        setattr(enum_base, variant_name, type(variant_name, (enum_base, variant), {}))
    return enum_base
