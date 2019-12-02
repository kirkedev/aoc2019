from typing import Tuple
from typing import NamedTuple
from typing import Iterator
from typing import Iterable
from typing import List
from enum import IntEnum
from itertools import takewhile
from itertools import zip_longest


class Operation(IntEnum):
    ADD = 1
    MULTIPLY = 2
    EXIT = 99


class Instruction(NamedTuple):
    operation: Operation
    first: int
    second: int
    address: int


def chunk(iterable: Iterable, size: int) -> Iterable[Tuple]:
    args = [iter(iterable)] * size
    return zip_longest(*args)


def instructions(memory: List[int]) -> Iterator[Instruction]:
    for group in takewhile(lambda it: it[0] != Operation.EXIT, chunk(memory, 4)):
        (operation, first, second, address) = group
        yield Instruction(operation, memory[first], memory[second], address)
