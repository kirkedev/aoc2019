from io import StringIO
from . import orbits
from . import total_orbits
from . import parse_input


def test_orbits_single():
    system = {
        'COM': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }

    assert orbits(system) == 3
    assert total_orbits(system) == 6


def test_orbits_multiple():
    system = {
        'COM': ['B'],
        'B': ['C', 'G'],
        'C': ['D'],
        'D': [],
        'G': ['H'],
        'H': []
    }

    assert orbits(system, 'COM') == 5
    assert orbits(system, 'B') == 4
    assert total_orbits(system) == 11


def test_parse_input():
    io = StringIO('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\n')
    system = parse_input(io)

    assert orbits(system, 'COM') == 11
    assert orbits(system, 'B') == 10
    assert orbits(system, 'C') == 7
    assert orbits(system, 'D') == 6
    assert orbits(system, 'E') == 4
    assert orbits(system, 'F') == 0
    assert orbits(system, 'G') == 1
    assert orbits(system, 'H') == 0
    assert orbits(system, 'I') == 0
    assert orbits(system, 'J') == 2
    assert orbits(system, 'K') == 1
    assert orbits(system, 'L') == 0

    assert total_orbits(system) == 42
