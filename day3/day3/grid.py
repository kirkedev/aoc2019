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


def step(position: Position, delta: Delta) -> Position:
    return position[0] + delta[0], position[1] + delta[1]


def move(start: Position, vector: Vector) -> Iterator[Position]:
    steps = accumulate(repeat(vector.direction.value, vector.distance), step, initial=start)  # type: ignore
    return islice(steps, 1, None)


def positions(vectors: Iterator[Vector]) -> List[Position]:
    position = (0, 0)
    result = [position]

    for vector in vectors:
        result.extend(move(position, vector))
        position = result[-1]

    return result


def intersections(first: List[Position], second: List[Position]) -> Iterable[Position]:
    return set(first[1:]).intersection(set(second[1:]))


def manhattan_distance(position: Position) -> int:
    left, top = position
    return abs(left) + abs(top)
