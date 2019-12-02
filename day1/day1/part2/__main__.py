from sys import stdin
from .. import parse_input
from .. import total_fuel

print(sum(map(total_fuel, parse_input(stdin))))
