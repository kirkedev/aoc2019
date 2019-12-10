from typing import Tuple
from typing import List
from typing import Optional
from .instruction import OpCode
from .instruction import Mode
from .instruction import parse_instructions


class Computer:
    memory: List[int]

    def __init__(self, codes: List[int], noun: Optional[int] = None, verb: Optional[int] = None):
        self.memory = memory = codes.copy()

        if noun is not None:
            memory[1] = noun

        if verb is not None:
            memory[2] = verb

    @property
    def result(self) -> int:
        return self.memory[0]

    def get_value(self, mode: Mode, param: int) -> int:
        return param if mode == Mode.IMMEDIATE else self.memory[param]

    def get_values(self, modes: int, first: int, second: int) -> Tuple[int, int]:
        return self.get_value(Mode(modes % 10), first), self.get_value(Mode(modes // 10), second)

    def add(self, modes: int, first: int, second: int, address: int) -> None:
        first_value, second_value = self.get_values(modes, first, second)
        self.memory[address] = first_value + second_value

    def multiply(self, modes: int, first: int, second: int, address: int) -> None:
        first_value, second_value = self.get_values(modes, first, second)
        self.memory[address] = first_value * second_value

    def less_than(self, modes: int, first: int, second: int, address: int) -> None:
        first_value, second_value = self.get_values(modes, first, second)
        self.memory[address] = 1 if first_value < second_value else 0

    def equals(self, modes: int, first: int, second: int, address: int) -> None:
        first_value, second_value = self.get_values(modes, first, second)
        self.memory[address] = 1 if first_value == second_value else 0

    def input(self, address: int) -> None:
        self.memory[address] = int(input(""))

    def output(self, address: int) -> None:
        print(self.memory[address])

    def run(self) -> int:
        for instructions in parse_instructions(self.memory):
            code = instructions[0]
            operation = code % 100
            modes = code // 100
            params = instructions[1:]

            if operation == OpCode.ADD:
                self.add(modes, *params)

            elif operation == OpCode.MULTIPLY:
                self.multiply(modes, *params)

            elif operation == OpCode.LESS_THAN:
                self.less_than(modes, *params)

            elif operation == OpCode.EQUALS:
                self.equals(modes, *params)

            elif operation == OpCode.OUTPUT:
                self.output(*params)

            elif operation == OpCode.INPUT:
                self.input(*params)

        return self.result
