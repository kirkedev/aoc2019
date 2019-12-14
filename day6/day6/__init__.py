from typing import Tuple
from typing import List
from typing import Dict
from typing import TextIO
from collections import defaultdict

System = Dict[str, List[str]]


def orbits(system: System, name: str = 'COM') -> int:
    ring = system.get(name)
    return 0 if ring is None else len(ring) + sum(orbits(system, name) for name in ring)


def total_orbits(system: System) -> int:
    return sum(orbits(system, name) for name in system.keys())


def parse_orbit(line: str) -> Tuple[str, str]:
    body, satellite = line.replace('\n', '').split(')')
    return body, satellite


def parse_input(io: TextIO) -> System:
    system = defaultdict(lambda: [])

    for body, satellite in map(parse_orbit, io):
        system[body].append(satellite)

    return system
