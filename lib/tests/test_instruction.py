from io import StringIO
from aoc.instruction import parse_input
from aoc.instruction import parse_instructions
from aoc.instruction import OpCode


def test_parse_input():
    io = StringIO("1,0,0,3,1\n")
    assert list(parse_input(io)) == [1, 0, 0, 3, 1]


def test_parse_instruction():
    codes = [2, 4, 4, 5, 99, 0]
    instruction = next(parse_instructions(codes))
    operation, first, second, address = instruction

    assert operation == OpCode.MULTIPLY
    assert first == 4
    assert second == 4
    assert address == 5


def test_parse_instructions():
    codes = [1, 0, 0, 0, 2, 3, 0, 3, 99]
    instructions = parse_instructions(codes)

    operation, first, second, address = next(instructions)
    assert operation == OpCode.ADD
    assert first == 0
    assert second == 0
    assert address == 0

    operation, first, second, address = next(instructions)
    assert operation == OpCode.MULTIPLY
    assert first == 3
    assert second == 0
    assert address == 3

    try:
        next(instructions)
        assert False
    except StopIteration:
        assert True
