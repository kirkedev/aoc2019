from typing import Iterator


def parse_input(lines: Iterator[str]) -> Iterator[int]:
    return map(int, lines)


def required_fuel(mass: int) -> int:
    return mass // 3 - 2


def total_fuel(mass: int) -> int:
    fuel = required_fuel(mass)
    return fuel + total_fuel(fuel) if fuel > 0 else 0
