from io import StringIO
from aoc.computer import Computer


def set_input(monkeypatch, value: str):
    monkeypatch.setattr('sys.stdin', StringIO(value))


def get_output(capsys):
    output, _ = capsys.readouterr()
    return output


def test_set_noun_and_verb():
    computer = Computer([1, 9, 10], 12, 2)
    assert computer.memory == [1, 12, 2]


def test_execute_program():
    computer = Computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    assert computer.run() == 3500
    assert computer.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_position_mode_equals_8(monkeypatch, capsys):
    codes = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1

    set_input(monkeypatch, '5')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0


def test_immediate_mode_equals_8(monkeypatch, capsys):
    codes = [3, 3, 1108, -1, 8, 3, 4, 3, 99]

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1

    set_input(monkeypatch, '10')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0


def test_position_mode_less_than_8(monkeypatch, capsys):
    codes = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]

    set_input(monkeypatch, '5')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0


def test_immediate_mode_less_than_8(monkeypatch, capsys):
    codes = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]

    set_input(monkeypatch, '5')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0


def test_jump_position_mode(monkeypatch, capsys):
    codes = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]

    set_input(monkeypatch, '0')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1


def test_jump_immediate_mode(monkeypatch, capsys):
    codes = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]

    set_input(monkeypatch, '0')
    Computer(codes).run()
    assert int(get_output(capsys)) == 0

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1


def test_computer_end_to_end(monkeypatch, capsys):
    codes = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    ]

    set_input(monkeypatch, '7')
    Computer(codes).run()
    assert int(get_output(capsys)) == 999

    set_input(monkeypatch, '8')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1000

    set_input(monkeypatch, '9')
    Computer(codes).run()
    assert int(get_output(capsys)) == 1001
