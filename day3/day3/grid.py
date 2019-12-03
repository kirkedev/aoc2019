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
Delta = Tuple[int, int]


class Direction(Enum):
    LEFT = 'L'
    UP = 'U'
    RIGHT = 'R'
    DOWN = 'D'

    @property
    def delta(self) -> Delta:
        return (-1, 0) if self == Direction.LEFT \
            else (0, -1) if self == Direction.UP \
            else (1, 0) if self == Direction.RIGHT \
            else (0, 1) if self == Direction.DOWN \
            else (0, 0)


class Vector(NamedTuple):
    direction: Direction
    distance: int


def step(position: Position, delta: Delta) -> Position:
    return position[0] + delta[0], position[1] + delta[1]


def move(start: Position, vector: Vector) -> Iterator[Position]:
    result = accumulate(repeat(vector.direction.delta, vector.distance), step, initial=start)  # type: ignore
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
