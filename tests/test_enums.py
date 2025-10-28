import pytest
from ape import AlgebraicEnum, VariantNotDataclassError, IndividualVariantMethodError
from dataclasses import dataclass


def test_non_dataclass_variant():
    with pytest.raises(VariantNotDataclassError):

        @AlgebraicEnum
        class Enum:
            class Variant1:
                pass

            class Variant2:
                pass


def test_variant_with_functions():
    with pytest.raises(IndividualVariantMethodError):

        @AlgebraicEnum
        class Enum:
            @dataclass
            class Variant1:
                theta: str
                epsilon: str

            @dataclass
            class Variant2:
                alpha: int
                beta: int

                def compute(self):
                    return self.alpha + self.beta


def test_sane_definition():
    @AlgebraicEnum
    class Enum:
        @dataclass
        class Variant1:
            theta: str
            epsilon: str

        @dataclass
        class Variant2:
            alpha: int
            beta: int

    v1 = Enum.Variant1("theta", "epsilon")
    v2 = Enum.Variant2(2, 4)

    assert isinstance(v1, Enum)
    assert isinstance(v2, Enum)


def test_minimal_sane_definition():
    @AlgebraicEnum
    class Enum:
        @dataclass
        class Variant1:
            pass

        @dataclass
        class Variant2:
            pass

    v1 = Enum.Variant1()
    v2 = Enum.Variant2()

    assert isinstance(v1, Enum)
    assert isinstance(v2, Enum)


def test_sane_definition_match_variants():
    @AlgebraicEnum
    class Enum:
        @dataclass
        class Variant1:
            theta: str
            epsilon: str

        @dataclass
        class Variant2:
            alpha: int
            beta: int

        def compute(self) -> int:
            match self:
                case self.Variant1(theta, epsilon):
                    return len(theta) + len(epsilon)

                case self.Variant2(alpha, beta):
                    return alpha + beta

    v1 = Enum.Variant1("theta", "epsilon")
    v2 = Enum.Variant2(2, 4)

    assert isinstance(v1, Enum)
    assert isinstance(v2, Enum)

    assert v1.compute() == 12
    assert v2.compute() == 6
