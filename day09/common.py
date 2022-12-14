from enum import Enum
from os.path import dirname, join
from typing import List, Set, Tuple


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


def perform_all_moves(
    knot_positions: List[Tuple[int, int]],
    positions_visited: Set[Tuple[int, int]],
):
    for move in generate_moves():
        perform_move(move, knot_positions, positions_visited)


def perform_move(
    move: Tuple[Direction, int],
    knot_positions: List[Tuple[int, int]],
    positions_visited: Set[Tuple[int, int]],
):
    direction, distance = move
    for _ in range(distance):
        knot_positions[0] = move_one_knot(knot_positions[0], direction)
        move_tail(knot_positions)

        positions_visited.add(knot_positions[-1])


def move_one_knot(
    knot_position: Tuple[int, int], direction: Direction
) -> Tuple[int, int]:
    x, y = knot_position
    if direction == Direction.UP:
        return (x, y + 1)
    if direction == Direction.DOWN:
        return (x, y - 1)
    if direction == Direction.LEFT:
        return (x - 1, y)
    if direction == Direction.RIGHT:
        return (x + 1, y)


def move_tail(knot_positions: List[Tuple[int, int]]):
    last_knot_moved = knot_positions[0]
    for i, position in enumerate(knot_positions[1:], 1):
        knot_positions[i] = move_trailing_knot(last_knot_moved, position)
        last_knot_moved = knot_positions[i]
    return last_knot_moved


def move_trailing_knot(
    position_leading: Tuple[int, int], position_trailing: Tuple[int, int]
) -> Tuple[int, int]:
    lx, ly = position_leading
    tx, ty = position_trailing

    # touching, no need to move
    if abs(lx - tx) in (0, 1) and abs(ly - ty) in (0, 1):
        return (tx, ty)

    # in same row
    if lx == tx:
        if ly < ty:
            return (tx, ty - 1)
        else:
            return (tx, ty + 1)

    # in same column
    if ly == ty:
        if lx < tx:
            return (tx - 1, ty)
        else:
            return (tx + 1, ty)

    # diagonal
    one_step_toward_leading_in_x = 1 if lx > tx else -1
    one_step_toward_leading_in_y = 1 if ly > ty else -1
    return (tx + one_step_toward_leading_in_x, ty + one_step_toward_leading_in_y)


def generate_moves():
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            direction, distance = line.strip().split()
            yield Direction(direction), int(distance)
