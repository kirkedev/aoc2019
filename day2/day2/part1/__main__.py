from sys import stdin
from .. import parse_input
from .. import calculate

print(calculate(parse_input(next(stdin)), 12, 2))
