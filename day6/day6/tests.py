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

    assert system['COM'] == ['B']
    assert system['B'] == ['C', 'G']
    assert system['C'] == ['D']
    assert system['D'] == ['E', 'I']
    assert system['E'] == ['F', 'J']
    assert system['G'] == ['H']
    assert system['J'] == ['K']
    assert system['K'] == ['L']

    assert system.get('F') is None
    assert system.get('H') is None
    assert system.get('I') is None
    assert system.get('L') is None

    assert total_orbits(system) == 42
