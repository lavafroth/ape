from dataclasses import dataclass
from typing import Tuple
from ape import AlgebraicEnum


@AlgebraicEnum
class Host:
    @dataclass
    class V4:
        octets: Tuple[int, int, int, int]

    @dataclass
    class V6:
        quartets: Tuple[int, int, int, int, int, int, int, int]

    def __str__(self):
        match self:
            case Host.V4(octets):
                return ".".join(map(str, octets))
            case Host.V6(quartets):
                return ":".join(f"{q:04x}" for q in quartets)


for host in (
    Host.V4((1, 1, 1, 1)),
    Host.V6((0x2011, 0xcdba, 0x1900, 0x0, 0x0, 0x0, 0x1757, 0x3818)),
):
    assert isinstance(host, Host)
    print(host)
