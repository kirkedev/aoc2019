from day1.part1.fuel import fuel_required


def test_mass_12():
    assert fuel_required(12) == 2


def test_mass_14():
    assert fuel_required(14) == 2


def test_mass_1969():
    assert fuel_required(1969) == 654


def test_mass_100756():
    assert fuel_required(100756) == 33583
