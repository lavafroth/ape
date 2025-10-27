from dataclasses import dataclass
from typing import Tuple
from abc import ABC


class Host(ABC):
    class __base:
        def __str__(self):
            match self:
                case Host.V4(octets):
                    return ".".join(map(str, octets))
                case Host.V6(quartet):
                    return ":".join(f"{q:04x}" for q in quartet)

    @dataclass
    class V4(__base):
        octets: Tuple[int, int, int, int]

    @dataclass
    class V6(__base):
        quartet: Tuple[int, int, int, int, int, int]


Host.register(Host.V4)
Host.register(Host.V6)


def main():
    for host in (
        Host.V4((1, 1, 1, 1)),
        Host.V6((1, 1, 1, 1, 1, 1)),
    ):
        assert isinstance(host, Host)
        print(host)


if __name__ == "__main__":
    main()
