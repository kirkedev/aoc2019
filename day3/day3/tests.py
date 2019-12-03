from io import StringIO
from .grid import Direction
from .grid import Vector
from . import parse_vector
from . import parse_wire
from . import parse_input


def test_parse_vector():
    vector = parse_vector('R', '994')
    assert vector.direction == Direction.RIGHT
    assert vector.distance == 994


def test_parse_wire():
    first, second = parse_wire(r'D213,L483\n')
    assert first.direction == Direction.DOWN
    assert first.distance == 213
    assert second.direction == Direction.LEFT
    assert second.distance == 483


def test_parse_input():
    first, second = parse_input(StringIO('U102,L292\nL1010,D906'))
    assert list(first) == [Vector(Direction.UP, 102), Vector(Direction.LEFT, 292)]
    assert list(second) == [Vector(Direction.LEFT, 1010), Vector(Direction.DOWN, 906)]
