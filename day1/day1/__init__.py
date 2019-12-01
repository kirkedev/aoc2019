from typing import Iterator
from sys import stdin


def read_input() -> Iterator[int]:
    return map(int, stdin)
