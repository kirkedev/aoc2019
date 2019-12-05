from typing import Iterable
from typing import TextIO
from collections import Counter


def parse_input(io: TextIO) -> Iterable[str]:
    start, end = map(int, next(io).split('-'))
    return map(str, range(start, end + 1))


def is_increasing(password: str) -> bool:
    return ''.join(sorted(password)) == password


def has_double(password: str) -> bool:
    return any(count >= 2 for _, count in Counter(password).most_common())


def has_exact_double(password: str) -> bool:
    return any(count == 2 for _, count in Counter(password).most_common())
