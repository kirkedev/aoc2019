from typing import List
from re import finditer
from .instruction import instructions
from .instruction import OpCode


def parse_input(line: str) -> List[int]:
    return list(map(lambda match: int(match[0]), finditer("\\d+", line)))


def execute(memory: List[int]) -> List[int]:
    for operator, first, second, position in instructions(memory):
        if operator == OpCode.ADD:
            memory[position] = first + second

        if operator == OpCode.MULTIPLY:
            memory[position] = first * second

    return memory


def get_result(codes: List[int], noun: int, verb: int) -> int:
    codes[1] = noun
    codes[2] = verb
    return execute(codes)[0]
