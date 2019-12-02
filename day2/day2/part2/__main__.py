from sys import stdin
from itertools import product
from .. import parse_input
from .. import calculate

codes = parse_input(next(stdin))

for (noun, verb) in product(range(100), repeat=2):
    if calculate(codes, noun, verb) == 19690720:
        print(noun * 100 + verb)
        break
