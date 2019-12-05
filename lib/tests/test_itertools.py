from aoc2019.itertools import chunk


def test_chunk():
    first, second = chunk([1, 2, 3, 4, 5, 6, 7], 4)
    assert list(first) == [1, 2, 3, 4]
    assert list(second) == [5, 6, 7, None]
