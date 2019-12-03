from typing import Tuple
from typing import Iterator
from typing import Iterable
from typing import List
from itertools import takewhile
from itertools import zip_longest
from .instruction import Operation
from .instruction import Instruction


def chunk(iterable: Iterable, size: int) -> Iterable[Tuple]:
    args = [iter(iterable)] * size
    return zip_longest(*args)


class Computer:
    memory: List[int]

    def __init__(self, codes: List[int]):
        self.memory = codes.copy()

    def set_noun(self, noun: int):
        self.memory[1] = noun

    def set_verb(self, verb: int):
        self.memory[2] = verb

    @property
    def result(self) -> int:
        return self.memory[0]

    @property
    def instructions(self) -> Iterator[Instruction]:
        memory = self.memory

        for group in takewhile(lambda it: it[0] != Operation.EXIT, chunk(memory, 4)):
            (operation, first, second, address) = group
            yield Instruction(operation, memory[first], memory[second], address)

    def execute_program(self):
        memory = self.memory

        for operation, first, second, address in self.instructions:
            if operation == Operation.ADD:
                memory[address] = first + second

            if operation == Operation.MULTIPLY:
                memory[address] = first * second
