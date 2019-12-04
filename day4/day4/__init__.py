from typing import Iterable
from typing import TextIO
from re import finditer


def parse_input(io: TextIO) -> Iterable[int]:
    return range(*map(int, next(io).split('-')))


def is_increasing(number: int) -> bool:
    password = str(number)
    return "".join(sorted(password)) == password


def has_double(number: int) -> bool:
    return any(finditer(r'(\d)\1+', str(number)))

