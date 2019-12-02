from typing import List
from re import finditer

from .computer import Computer
from .instruction import Operation
from .instruction import instructions


def parse_input(line: str) -> List[int]:
    return list(map(lambda match: int(match[0]), finditer("\\d+", line)))


def calculate(codes: List[int], noun: int, verb: int) -> int:
    model = Computer(codes)
    model.set_noun(noun)
    model.set_verb(verb)
    model.execute_program()
    return model.result
