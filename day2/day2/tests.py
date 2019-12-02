from io import StringIO
from . import parse_input
from . import calculate
from .instruction import Operation
from .instruction import instructions
from .computer import Computer


def test_parse_input():
    io = StringIO("1,0,0,3,1\n")
    line = next(io)
    assert list(parse_input(line)) == [1, 0, 0, 3, 1]


def test_parse_instruction():
    io = StringIO("2,4,4,5,99,0\n")
    line = next(io)
    codes = parse_input(line)
    instruction = next(instructions(codes))

    assert instruction.operation == Operation.MULTIPLY
    assert instruction.first == 99
    assert instruction.second == 99
    assert instruction.address == 5


def test_parse_instructions():
    io = StringIO("1,0,0,0,2,3,0,3,99\n")
    line = next(io)
    codes = parse_input(line)
    first, second = instructions(codes)

    assert first.operation == Operation.ADD
    assert first.first == 1
    assert first.second == 1
    assert first.address == 0

    assert second.operation == Operation.MULTIPLY
    assert second.first == 0
    assert second.second == 1
    assert second.address == 3


def test_execute_program():
    io = StringIO("1,9,10,3,2,3,11,0,99,30,40,50\n")
    line = next(io)
    computer = Computer(parse_input(line))
    computer.execute_program()
    assert computer.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_calculate():
    io = StringIO("1,2,2,4,99,5,6,0,99\n")
    line = next(io)
    assert calculate(parse_input(line), 1, 1) == 30
