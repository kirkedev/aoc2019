from sys import stdin
from itertools import product
from aoc.instruction import parse_input
from .. import calculate

codes = parse_input(stdin)
noun, verb = next(pair for pair in product(range(100), repeat=2) if calculate(codes, *pair) == 19690720)
print(noun * 100 + verb)
