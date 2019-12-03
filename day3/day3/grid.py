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
Delta = Tuple[int, int]


class Direction(Enum):
    L = LEFT = (-1, 0)
    U = UP = (0, -1)
    R = RIGHT = (1, 0)
    D = DOWN = (0, 1)


class Vector(NamedTuple):
    direction: Direction
    distance: int


def step(position: Position, direction: Delta) -> Position:
    return position[0] + direction[0], position[1] + direction[1]


def move(start: Position, vector: Vector) -> Iterator[Position]:
    result = accumulate(repeat(vector.direction.value, vector.distance), step, initial=start)  # type: ignore
    return islice(result, 1, None)


def positions(vectors: Iterator[Vector]) -> List[Position]:
    result: List[Position] = []
    position = (0, 0)

    for vector in vectors:
        result.extend(move(position, vector))
        position = result[-1]

    return result


def intersections(first: Iterable[Position], second: Iterable[Position]) -> Iterable[Position]:
    return set(first).intersection(set(second))


def manhattan_distance(position: Position) -> int:
    left, top = position
    return abs(left) + abs(top)
