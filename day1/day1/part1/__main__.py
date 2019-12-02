from sys import stdin
from .. import parse_input
from .. import required_fuel

print(sum(map(required_fuel, parse_input(stdin))))
