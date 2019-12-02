from sys import stdin
from itertools import product
from .. import parse_input
from .. import get_result

puzzle = parse_input(next(stdin))

for (noun, verb) in product(range(100), repeat=2):
    if get_result(puzzle.copy(), noun, verb) == 19690720:
        print(noun * 100 + verb)
        break
