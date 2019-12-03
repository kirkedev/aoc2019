from typing import Tuple
from typing import Iterator
from typing import Iterable
from typing import List
from typing import TypeVar
from itertools import takewhile
from itertools import zip_longest
from .instruction import Operation
from .instruction import Instruction

T = TypeVar('T')


def chunk(iterable: Iterable[T], size: int) -> Iterable[Tuple[T, ...]]:
    args = [iter(iterable)] * size
    return zip_longest(*args)


class Computer:
    memory: List[int]

    def __init__(self, codes: List[int]):
        self.memory = codes.copy()

    def set_noun(self, noun: int) -> None:
        self.memory[1] = noun

    def set_verb(self, verb: int) -> None:
        self.memory[2] = verb

    @property
    def result(self) -> int:
        return self.memory[0]

    @property
    def instructions(self) -> Iterator[Instruction]:
        memory = self.memory

        for (operation, first, second, address) in takewhile(lambda it: it[0] != Operation.EXIT, chunk(memory, 4)):
            yield Instruction(Operation(operation), memory[first], memory[second], address)

    def execute_program(self) -> None:
        memory = self.memory

        for operation, first, second, address in self.instructions:
            if operation == Operation.ADD:
                memory[address] = first + second

            if operation == Operation.MULTIPLY:
                memory[address] = first * second
