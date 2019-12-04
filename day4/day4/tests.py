from io import StringIO
from . import parse_input, is_increasing, has_double, exactly_double


def test_parse_input():
    assert parse_input(StringIO('246515-739105\n')) == range(246515, 739105)


def test_is_increasing():
    assert is_increasing(111111) is True
    assert is_increasing(123789) is True
    assert is_increasing(223450) is False


def test_has_double():
    assert has_double(223450) is True
    assert has_double(111111) is True
    assert has_double(123789) is False


def test_exactly_double():
    assert exactly_double(112233) is True
    assert exactly_double(123444) is False
    assert exactly_double(111122) is True
