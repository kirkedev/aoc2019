from sys import stdin
from aoc.instruction import parse_input
from .. import calculate

print(calculate(parse_input(stdin), noun=12, verb=2))
