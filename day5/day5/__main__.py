from sys import stdin
from aoc.computer import Computer
from aoc.instruction import parse_input

Computer(parse_input(stdin)).run()
