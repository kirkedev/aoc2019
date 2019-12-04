from sys import stdin
from .. import parse_input
from .. import is_increasing
from .. import has_exact_double


print(sum(1 for password in parse_input(stdin) if is_increasing(password) and has_exact_double(password)))
