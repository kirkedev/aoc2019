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

    def add(self, modes: int, first: int, second: int, address: int) -> None:
        memory = self.memory
        first_value = first if modes % 10 == Mode.IMMEDIATE else memory[first]
        second_value = second if modes // 10 == Mode.IMMEDIATE else memory[second]
        memory[address] = first_value + second_value

    def multiply(self, modes: int, first: int, second: int, address: int) -> None:
        memory = self.memory
        first_value = first if modes % 10 == Mode.IMMEDIATE else memory[first]
        second_value = second if modes // 10 == Mode.IMMEDIATE else memory[second]
        memory[address] = first_value * second_value

    def output(self, modes: int, param: int) -> None:
        value = param if modes % 10 == Mode.IMMEDIATE else self.memory[param]
        print(value)

    def input(self, address: int) -> None:
        self.memory[address] = int(input(""))

    def execute_program(self) -> int:
        for instructions in parse_instructions(self.memory):
            code = instructions[0]
            operation = code % 100
            modes = code // 100
            params = instructions[1:]

            if operation == OpCode.ADD:
                self.add(modes, *params)

            elif operation == OpCode.MULTIPLY:
                self.multiply(modes, *params)

            elif operation == OpCode.OUTPUT:
                self.output(modes, *params)

            elif operation == OpCode.INPUT:
                self.input(*params)

        return self.result
