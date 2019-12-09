from typing import List
from aoc.computer import Computer


def calculate(codes: List[int], noun: int, verb: int) -> int:
    return Computer(codes, noun=noun, verb=verb).run()
