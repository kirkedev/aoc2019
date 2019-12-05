from io import StringIO
from .grid import Direction
from .grid import Vector
from .grid import move
from .grid import positions
from .grid import intersections
from . import parse_vector
from . import parse_wire
from . import parse_input
from . import closest_intersection
from . import shortest_intersection


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


def test_move():
    assert list(move((0, 0), Direction.RIGHT, 3)) == [(1, 0), (2, 0), (3, 0)]


def test_positions():
    wire = parse_wire('R8,U5,L5,D3')

    assert positions(wire) == [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
        (8, -1), (8, -2), (8, -3), (8, -4), (8, -5),
        (7, -5), (6, -5), (5, -5), (4, -5), (3, -5),
        (3, -4), (3, -3), (3, -2)
    ]


def test_intersection():
    io = StringIO('R8,U5,L5,D3\nU7,R6,D4,L4')
    first, second = map(positions, parse_input(io))
    assert list(intersections(first, second)) == [(6, -5), (3, -3)]


def test_closest_intersection():
    io = StringIO('R8,U5,L5,D3\nU7,R6,D4,L4')
    assert closest_intersection(parse_input(io)) == 6

    io = StringIO('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83')
    assert closest_intersection(parse_input(io)) == 159

    io = StringIO('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
    assert closest_intersection(parse_input(io)) == 135


def test_shortest_intersection():
    io = StringIO('R8,U5,L5,D3\nU7,R6,D4,L4')
    assert shortest_intersection(parse_input(io)) == 30

    io = StringIO('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83')
    assert shortest_intersection(parse_input(io)) == 610

    io = StringIO('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
    assert shortest_intersection(parse_input(io)) == 410
