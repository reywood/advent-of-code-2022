from part1 import move_tail


def test_should_not_move_if_same_position():
    assert move_tail((0, 0), (0, 0)) == (0, 0)


def test_should_not_move_if_touching_diagonally():
    diagonal_scenarios = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for head in diagonal_scenarios:
        new_tail = move_tail(head, (0, 0))
        assert new_tail == (0, 0)


def test_should_not_move_if_touching_horizontally():
    new_tail = move_tail((-1, 0), (0, 0))
    assert new_tail == (0, 0)

    new_tail = move_tail((1, 0), (0, 0))
    assert new_tail == (0, 0)


def test_should_move_horizontally():
    new_tail = move_tail((-2, 0), (0, 0))
    assert new_tail == (-1, 0)

    new_tail = move_tail((2, 0), (0, 0))
    assert new_tail == (1, 0)


def test_should_not_move_if_touching_vertically():
    new_tail = move_tail((0, -1), (0, 0))
    assert new_tail == (0, 0)

    new_tail = move_tail((0, 1), (0, 0))
    assert new_tail == (0, 0)


def test_should_move_vertically():
    new_tail = move_tail((0, -2), (0, 0))
    assert new_tail == (0, -1)

    new_tail = move_tail((0, 2), (0, 0))
    assert new_tail == (0, 1)


def test_should_move_diagonally():
    new_tail = move_tail((1, -2), (0, 0))
    assert new_tail == (1, -1)

    new_tail = move_tail((1, 2), (0, 0))
    assert new_tail == (1, 1)

    new_tail = move_tail((-1, 2), (0, 0))
    assert new_tail == (-1, 1)

    new_tail = move_tail((-1, -2), (0, 0))
    assert new_tail == (-1, -1)

    new_tail = move_tail((2, 1), (0, 0))
    assert new_tail == (1, 1)

    new_tail = move_tail((3, 1), (1, 2))
    assert new_tail == (2, 1)

    new_tail = move_tail((3, 3), (1, 1))
    assert new_tail == (2, 2)
