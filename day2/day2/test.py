from io import StringIO
from . import OpCode
from . import parse_input
from . import commands
from . import program
from . import get_result


def test_parse_input():
    io = StringIO("1,0,0,3,1\n")
    line = next(io)
    assert list(parse_input(line)) == [1, 0, 0, 3, 1]


def test_parse_command():
    io = StringIO("2,4,4,5,99,0\n")
    line = next(io)
    codes = parse_input(line)
    command = next(commands(codes))

    assert command.code == OpCode.MULTIPLY
    assert command.first == 99
    assert command.second == 99
    assert command.position == 5


def test_parse_commands():
    io = StringIO("1,0,0,0,2,3,0,3,99\n")
    line = next(io)
    codes = parse_input(line)
    first, second = commands(codes)

    assert first.code == OpCode.ADD
    assert first.first == 1
    assert first.second == 1
    assert first.position == 0

    assert second.code == OpCode.MULTIPLY
    assert second.first == 0
    assert second.second == 1
    assert second.position == 3


def test_program():
    io = StringIO("1,1,1,4,99,5,6,0,99\n")
    line = next(io)
    assert program(parse_input(line)) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_get_result():
    io = StringIO("1,2,2,4,99,5,6,0,99\n")
    line = next(io)
    assert get_result(parse_input(line), 1, 1) == 30
