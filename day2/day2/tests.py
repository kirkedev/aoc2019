from io import StringIO
from aoc.instruction import parse_input
from . import calculate


def test_calculate():
    io = StringIO("1,2,2,4,99,5,6,0,99\n")
    assert calculate(parse_input(io), 1, 1) == 30
