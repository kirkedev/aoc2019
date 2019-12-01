from ..fuel import fuel_required
from ..fuel import fuel_requirements
from ..fuel import total_fuel


def test_mass_12():
    assert fuel_required(12) == 2


def test_mass_14():
    assert fuel_required(14) == 2


def test_mass_1969():
    assert fuel_required(1969) == 654


def test_mass_100756():
    assert fuel_required(100756) == 33583


def test_fuel_mass_654():
    assert list(fuel_requirements(654)) == [216, 70, 21, 5]


def test_fuel_mass_33583():
    assert list(fuel_requirements(33583)) == [11192, 3728, 1240, 411, 135, 43, 12, 2]


def test_total_fuel_14():
    assert total_fuel(14) == 2


def test_total_fuel_1969():
    assert total_fuel(1969) == 966


def test_total_fuel_100756():
    assert total_fuel(100756) == 50346
