from typing import NamedTuple, Iterable
from typing import Iterator
from typing import List
from enum import IntEnum
from re import finditer
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


def parse_input(line: str) -> List[int]:
    return list(map(lambda match: int(match[0]), finditer("\\d+", line)))


def instructions(memory: List[int]) -> Iterator[Instruction]:
    for group in takewhile(lambda it: it[0] != OpCode.EXIT, chunk(memory, 4)):
        (code, first, second, address) = group
        yield Instruction(code=code, first=memory[first], second=memory[second], address=address)


def execute(memory: List[int]) -> List[int]:
    for instruction in instructions(memory):
        operator, first, second, position = instruction

        if operator == OpCode.ADD:
            memory[position] = first + second

        if operator == OpCode.MULTIPLY:
            memory[position] = first * second

    return memory


def get_result(codes: List[int], noun: int, verb: int) -> int:
    codes[1] = noun
    codes[2] = verb
    return execute(codes)[0]
