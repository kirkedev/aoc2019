from typing import NamedTuple
from typing import Iterator
from typing import Iterable
from typing import List
from enum import IntEnum
from itertools import takewhile
from itertools import zip_longest


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    EXIT = 99


class Instruction(NamedTuple):
    code: OpCode
    first: int
    second: int
    address: int


def chunk(iterable: Iterable, size: int):
    args = [iter(iterable)] * size
    return zip_longest(*args)


def instructions(memory: List[int]) -> Iterator[Instruction]:
    for group in takewhile(lambda it: it[0] != OpCode.EXIT, chunk(memory, 4)):
        (code, first, second, address) = group
        yield Instruction(code=code, first=memory[first], second=memory[second], address=address)
