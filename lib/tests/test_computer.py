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
    computer.run()
    assert computer.memory == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert computer.result == 3500


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
