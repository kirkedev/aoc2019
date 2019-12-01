from typing import Iterator


def fuel_required(mass: int) -> int:
    return mass // 3 - 2


def fuel_requirements(mass: int) -> Iterator[int]:
    mass = fuel_required(mass)

    while mass > 0:
        yield mass
        mass = fuel_required(mass)


def total_fuel(mass: int) -> int:
    return sum(fuel_requirements(mass))
