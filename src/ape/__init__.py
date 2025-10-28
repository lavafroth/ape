import inspect
from dataclasses import is_dataclass


def AlgebraicEnum(enum_base):
    for variant_name, variant in inspect.getmembers(enum_base, predicate=inspect.isclass):
        if variant_name == "__class__":
            continue

        if not is_dataclass(variant):
            raise Exception(
                f"AlgebraicEnum variants are required to be dataclasses. Consider adding the `@dataclass` decorator to variant `{variant_name}`."
            )

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
            raise Exception(
                f"Functions must not be declared on individual enum variants, found functions declared on variant {variant_name}: {', '.join(extra_declared_functions)}."
            )
        setattr(enum_base, variant_name, type(variant_name, (enum_base, variant), {}))
    return enum_base
