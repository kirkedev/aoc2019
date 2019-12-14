from typing import List
from typing import Dict
from typing import TextIO

System = Dict[str, List[str]]


def orbits(system: System, name: str = 'COM') -> int:
    ring = system.get(name)
    return 0 if ring is None else len(ring) + sum(orbits(system, name) for name in ring)


def total_orbits(system: System) -> int:
    return sum(orbits(system, name) for name in system.keys())


def parse_input(io: TextIO) -> System:
    system = {'COM': []}

    for line in io:
        body, satellite = line.replace('\n', '').split(')')

        if body not in system:
            system[body] = []

        system[body] += satellite

    return system
