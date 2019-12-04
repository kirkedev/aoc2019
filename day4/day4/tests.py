from io import StringIO
from . import parse_input
from . import is_increasing
from . import has_double
from . import has_exact_double


def test_parse_input():
    passwords = parse_input(StringIO('246515-739105\n'))
    first, second, *_, last = passwords
    assert first == '246515'
    assert second == '246516'
    assert last == '739105'


def test_is_increasing():
    assert is_increasing('111111') is True
    assert is_increasing('123789') is True
    assert is_increasing('223450') is False


def test_has_double():
    assert has_double('223450') is True
    assert has_double('111111') is True
    assert has_double('123789') is False


def test_exactly_double():
    assert has_exact_double('112233') is True
    assert has_exact_double('123444') is False
    assert has_exact_double('111122') is True
