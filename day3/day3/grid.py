from typing import Tuple
from typing import NamedTuple
from typing import Iterator
from typing import Iterable
from typing import List
from itertools import accumulate
from itertools import repeat
from itertools import islice
from enum import Enum

Position = Tuple[int, int]


class Direction(Enum):
    LEFT = 'L'
    UP = 'U'
    RIGHT = 'R'
    DOWN = 'D'


class Vector(NamedTuple):
    direction: Direction
    distance: int


def add_tuples(first: Tuple[int, int], second: Tuple[int, int]) -> Tuple[int, int]:
    return first[0] + second[0], first[1] + second[1]


def move(start: Position, vector: Vector) -> Iterator[Position]:
    direction = vector.direction

    step = (-1, 0) if direction == Direction.LEFT \
        else (0, -1) if direction == Direction.UP \
        else (1, 0) if direction == Direction.RIGHT \
        else (0, 1) if direction == Direction.DOWN \
        else (0, 0)

    result = accumulate(repeat(step, vector.distance), add_tuples, initial=start)  # type: ignore
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
