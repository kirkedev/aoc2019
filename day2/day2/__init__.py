from typing import NamedTuple
from typing import Iterator
from typing import List
from enum import IntEnum
from re import finditer
from itertools import islice


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    EXIT = 99


class Instruction(NamedTuple):
    code: OpCode
    first: int
    second: int
    position: int


def parse_input(line: str) -> List[int]:
    return list(map(lambda match: int(match[0]), finditer("\\d+", line)))


def instructions(codes: List[int]) -> Iterator[Instruction]:
    position = 0
    code = codes[position]

    while code != OpCode.EXIT:
        (first, second, storage) = islice(codes, position + 1, position + 4)
        yield Instruction(code=OpCode(code), first=codes[first], second=codes[second], position=storage)
        position += 4
        code = codes[position]


def program(codes: List[int]) -> List[int]:
    for instruction in instructions(codes):
        operator, first, second, position = instruction

        if operator == OpCode.ADD:
            codes[position] = first + second

        if operator == OpCode.MULTIPLY:
            codes[position] = first * second

    return codes


def get_result(codes: List[int], noun: int, verb: int) -> int:
    codes[1] = noun
    codes[2] = verb
    return program(codes)[0]
