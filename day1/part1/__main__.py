from sys import stdin
from .fuel import fuel_required

print(sum(map(fuel_required, map(int, stdin))))
