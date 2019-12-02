from io import StringIO
from . import parse_input
from . import execute
from . import get_result
from .instruction import OpCode
from .instruction import instructions


def test_parse_input():
    io = StringIO("1,0,0,3,1\n")
    line = next(io)
    assert list(parse_input(line)) == [1, 0, 0, 3, 1]


def test_parse_instruction():
    io = StringIO("2,4,4,5,99,0\n")
    line = next(io)
    codes = parse_input(line)
    instruction = next(instructions(codes))

    assert instruction.code == OpCode.MULTIPLY
    assert instruction.first == 99
    assert instruction.second == 99
    assert instruction.address == 5


def test_parse_instructions():
    io = StringIO("1,0,0,0,2,3,0,3,99\n")
    line = next(io)
    codes = parse_input(line)
    first, second = instructions(codes)

    assert first.code == OpCode.ADD
    assert first.first == 1
    assert first.second == 1
    assert first.address == 0

    assert second.code == OpCode.MULTIPLY
    assert second.first == 0
    assert second.second == 1
    assert second.address == 3


def test_execute():
    io = StringIO("1,9,10,3,2,3,11,0,99,30,40,50\n")
    line = next(io)
    assert execute(parse_input(line)) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_get_result():
    io = StringIO("1,2,2,4,99,5,6,0,99\n")
    line = next(io)
    assert get_result(parse_input(line), 1, 1) == 30
