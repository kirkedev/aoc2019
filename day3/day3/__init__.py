from typing import Iterator
from re import finditer
from .grid import Direction
from .grid import Vector
from .grid import positions
from .grid import intersections
from .grid import manhattan_distance

Wire = Iterator[Vector]
vector = r'([LURD])(\d+)'


def parse_vector(direction: str, distance: str) -> Vector:
    return Vector(direction=Direction[direction], distance=int(distance))


def parse_wire(line: str) -> Wire:
    return map(lambda match: parse_vector(*match.groups()), finditer(vector, line))


def parse_input(lines: Iterator[str]) -> Iterator[Wire]:
    return map(parse_wire, lines)


def closest_intersection(wires: Iterator[Wire]) -> int:
    first, second = map(positions, wires)
    return min(map(manhattan_distance, intersections(first, second)))


def shortest_intersection(wires: Iterator[Wire]) -> int:
    first, second = map(positions, wires)
    return min(map(lambda it: first.index(it) + 1 + second.index(it) + 1, intersections(first, second)))
