from sys import stdin
from itertools import product
from .. import parse_input
from .. import calculate

codes = parse_input(next(stdin))
inputs = product(range(100), repeat=2)
matches = filter(lambda pair: calculate(codes, *pair) == 19690720, inputs)
noun, verb = next(matches)

print(noun * 100 + verb)
