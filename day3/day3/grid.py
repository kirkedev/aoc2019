from typing import Tuple
from typing import NamedTuple
from enum import Enum

Position = Tuple[int, int]


class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'


class Vector(NamedTuple):
    direction: Direction
    distance: int
