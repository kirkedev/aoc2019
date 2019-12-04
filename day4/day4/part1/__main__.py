from sys import stdin
from .. import parse_input
from .. import is_increasing
from .. import has_double


print(sum(1 for password in parse_input(stdin) if is_increasing(password) and has_double(password)))
