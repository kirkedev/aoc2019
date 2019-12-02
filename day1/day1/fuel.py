def fuel_required(mass: int) -> int:
    return mass // 3 - 2


def total_fuel(mass: int) -> int:
    fuel = fuel_required(mass)
    return fuel + total_fuel(fuel) if fuel > 0 else 0
