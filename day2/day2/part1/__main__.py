from sys import stdin
from .. import parse_input
from .. import calculate

print(calculate(parse_input(next(stdin)), noun=12, verb=2))
