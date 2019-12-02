from typing import Iterator
from sys import stdin


def read_input() -> Iterator[int]:
    return map(int, stdin)


def required_fuel(mass: int) -> int:
    return mass // 3 - 2


def total_fuel(mass: int) -> int:
    fuel = required_fuel(mass)
    return fuel + total_fuel(fuel) if fuel > 0 else 0
