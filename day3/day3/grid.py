from typing import Tuple
from typing import NamedTuple
from typing import Iterator
from typing import Iterable
from typing import List
from enum import Enum
from itertools import accumulate
from itertools import repeat
from itertools import islice

Position = Tuple[int, int]


class Direction(Enum):
    L = LEFT = (-1, 0)
    U = UP = (0, -1)
    R = RIGHT = (1, 0)
    D = DOWN = (0, 1)


class Vector(NamedTuple):
    direction: Direction
    distance: int


def step(position: Position, direction: Direction) -> Position:
    left, top = direction.value
    return position[0] + left, position[1] + top


def move(start: Position, direction: Direction, distance: int) -> Iterator[Position]:
    return islice(accumulate(repeat(direction, distance), step, initial=start), 1, None)  # type: ignore


def positions(vectors: Iterator[Vector]) -> List[Position]:
    position = (0, 0)
    result = [position]

    for vector in vectors:
        result.extend(move(position, *vector))
        position = result[-1]

    return result


def intersections(first: List[Position], second: List[Position]) -> Iterable[Position]:
    return set(first[1:]).intersection(set(second[1:]))


def manhattan_distance(position: Position) -> int:
    left, top = position
    return abs(left) + abs(top)
