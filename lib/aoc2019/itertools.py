from typing import Iterable
from typing import TypeVar
from typing import Tuple
from itertools import zip_longest

T = TypeVar('T')


def chunk(iterable: Iterable[T], size: int) -> Iterable[Tuple[T, ...]]:
    args = [iter(iterable)] * size
    return zip_longest(*args)
