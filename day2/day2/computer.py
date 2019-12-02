from typing import List

from .instruction import Operation
from .instruction import instructions


class Computer:
    memory: List[int]

    def __init__(self, codes: List[int]):
        self.memory = codes.copy()

    def set_noun(self, noun):
        self.memory[1] = noun

    def set_verb(self, verb):
        self.memory[2] = verb

    @property
    def result(self) -> int:
        return self.memory[0]

    def execute_program(self):
        memory = self.memory

        for operator, first, second, address in instructions(memory):
            if operator == Operation.ADD:
                memory[address] = first + second

            if operator == Operation.MULTIPLY:
                memory[address] = first * second
