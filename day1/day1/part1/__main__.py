from .. import read_input
from .. import required_fuel

print(sum(map(required_fuel, read_input())))
