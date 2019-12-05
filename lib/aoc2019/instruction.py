from typing import NamedTuple
from enum import IntEnum


class Operation(IntEnum):
    ADD = 1
    MULTIPLY = 2
    EXIT = 99


class Instruction(NamedTuple):
    operation: Operation
    first: int
    second: int
    address: int
