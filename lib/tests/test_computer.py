from aoc.computer import Computer


def test_set_noun_and_verb():
    codes = [1, 9, 10]
    computer = Computer(codes, 12, 2)
    assert computer.memory == [1, 12, 2]


def test_execute_program():
    codes = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    computer = Computer(codes)
    computer.execute_program()
    assert computer.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert computer.result == 3500
