from typing import Tuple
from typing import List
from typing import Optional
from .instruction import OpCode
from .instruction import Position
from .instruction import parse_instructions
from .instruction import is_immediate_mode


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

    def get_value(self, modes: int, param: int, position: Position) -> int:
        return param if is_immediate_mode(modes, position) else self.memory[param]

    def get_values(self, modes: int, first: int, second: int) -> Tuple[int, int]:
        return self.get_value(modes, first, 1), self.get_value(modes, second, 2)

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

    def output(self, modes: int, address: int) -> None:
        value = self.get_value(modes, address, 1)
        print(value)

    def run(self, offset: int = 0) -> int:
        for instructions in parse_instructions(self.memory, offset):
            operation, modes, *params = instructions

            if operation == OpCode.ADD:
                self.add(modes, *params)

            elif operation == OpCode.MULTIPLY:
                self.multiply(modes, *params)

            elif operation == OpCode.LESS_THAN:
                self.less_than(modes, *params)

            elif operation == OpCode.EQUALS:
                self.equals(modes, *params)

            elif operation == OpCode.OUTPUT:
                self.output(modes, *params)

            elif operation == OpCode.INPUT:
                self.input(*params)

            elif operation == OpCode.JUMP_IF_TRUE:
                value, offset = self.get_values(modes, *params)
                if value != 0:
                    return self.run(offset)

            elif operation == OpCode.JUMP_IF_FALSE:
                value, offset = self.get_values(modes, *params)
                if value == 0:
                    return self.run(offset)

        return self.result
