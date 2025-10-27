from dataclasses import dataclass
from typing import Tuple
import inspect


def AlgebraicEnum(cls):
    for subclass_name, subclass in inspect.getmembers(cls, predicate=inspect.isclass):
        if subclass_name != "__class__":
            setattr(cls, subclass_name, type(subclass_name, (cls, subclass), {}))

    return cls


@AlgebraicEnum
class Host:
    @dataclass
    class V4:
        octets: Tuple[int, int, int, int]

    @dataclass
    class V6:
        quartets: Tuple[int, int, int, int, int, int]

    def __str__(self):
        match self:
            case Host.V4(octets):
                return ".".join(map(str, octets))
            case Host.V6(quartets):
                return ":".join(f"{q:04x}" for q in quartets)


def main():
    for host in (
        Host.V4((1, 1, 1, 1)),
        Host.V6((1, 1, 1, 1, 1, 1)),
    ):
        assert isinstance(host, Host)
        print(host)


if __name__ == "__main__":
    main()
