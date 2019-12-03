from typing import Iterator
from re import finditer
from .grid import Direction
from .grid import Vector

Wire = Iterator[Vector]
vector = r'([LURD])(\d+)'


def parse_vector(direction: str, distance: str) -> Vector:
    return Vector(direction=Direction(direction), distance=int(distance))


def parse_wire(line: str) -> Wire:
    return map(lambda match: parse_vector(*match.groups()), finditer(vector, line))


def parse_input(lines: Iterator[str]) -> Iterator[Wire]:
    return map(parse_wire, lines)
