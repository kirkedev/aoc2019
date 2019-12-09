from typing import Tuple
from typing import Iterator
from typing import List
from typing import TextIO
from enum import IntEnum
from re import finditer


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    EXIT = 99


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


def parse_instructions(memory: List[int]) -> Iterator[Tuple[int, ...]]:
    start = 0

    while True:
        code = memory[start]
        operation = code % 100

        if code == OpCode.EXIT:
            break

        length = 4 if operation in (OpCode.ADD, OpCode.MULTIPLY, OpCode.LESS_THAN, OpCode.EQUALS) \
            else 3 if operation in (OpCode.JUMP_IF_TRUE, OpCode.JUMP_IF_FALSE) \
            else 2 if operation in (OpCode.INPUT, OpCode.OUTPUT) \
            else 1

        end = start + length
        params = tuple(memory[start:end])

        if code == OpCode.JUMP_IF_TRUE:
            _, value, address = params
            value = value if code % 10 == Mode.IMMEDIATE else memory[value]
            start = address if value != 0 else end
            continue

        if code == OpCode.JUMP_IF_FALSE:
            _, value, address = params
            value = value if code % 10 == Mode.IMMEDIATE else memory[value]
            start = address if value == 0 else end
            continue

        yield params
        start = end


def parse_input(io: TextIO) -> List[int]:
    return list(map(lambda match: int(match[0]), finditer(r'-?\d+', next(io))))
