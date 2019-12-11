from typing import Literal
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


Instruction = Tuple[int, ...]
Position = Literal[1, 2]


def split_code(code: int) -> Tuple[OpCode, int]:
    operation = code % 100
    modes = code // 100
    return OpCode(operation), int(str(modes), 2)


def is_immediate_mode(mask: int, position: Position) -> bool:
    return mask & position == position


def parse_instructions(memory: List[int], offset: int = 0) -> Iterator[Instruction]:
    while True:
        operation, modes = split_code(memory[offset])

        if operation == OpCode.EXIT:
            break

        length = 4 if operation in (OpCode.ADD, OpCode.MULTIPLY, OpCode.LESS_THAN, OpCode.EQUALS) \
            else 3 if operation in (OpCode.JUMP_IF_TRUE, OpCode.JUMP_IF_FALSE) \
            else 2 if operation in (OpCode.INPUT, OpCode.OUTPUT) \
            else 1

        end = offset + length
        params = memory[offset + 1:end]
        yield operation, modes, *params
        offset = end


def parse_input(io: TextIO) -> List[int]:
    return list(int(match[0]) for match in finditer(r'-?\d+', next(io)))
