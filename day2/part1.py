POINTS_FOR_WIN = 6
POINTS_FOR_DRAW = 3
POINTS_FOR_LOSS = 0

PLAYER1_ROCK = "A"
PLAYER1_PAPER = "B"
PLAYER1_SCISSORS = "C"

PLAYER2_ROCK = "X"
PLAYER2_PAPER = "Y"
PLAYER2_SCISSORS = "Z"

SHAPE_POINTS = {
    PLAYER2_ROCK: 1,
    PLAYER2_PAPER: 2,
    PLAYER2_SCISSORS: 3,
}


def main():
    player2_points_per_round = [
        calculate_player2_points_for_round(player1_shape, player2_shape)
        for player1_shape, player2_shape in generate_rounds()
    ]

    print(player2_points_per_round)
    print(sum(player2_points_per_round))


def calculate_player2_points_for_round(player1_shape, player2_shape):
    if is_win_for_player2(player1_shape, player2_shape):
        return POINTS_FOR_WIN + SHAPE_POINTS[player2_shape]

    if is_draw(player1_shape, player2_shape):
        return POINTS_FOR_DRAW + SHAPE_POINTS[player2_shape]

    return POINTS_FOR_LOSS + SHAPE_POINTS[player2_shape]


def is_win_for_player2(player1_shape, player2_shape):
    return (
        (player1_shape == PLAYER1_ROCK and player2_shape == PLAYER2_PAPER)
        or (player1_shape == PLAYER1_PAPER and player2_shape == PLAYER2_SCISSORS)
        or (player1_shape == PLAYER1_SCISSORS and player2_shape == PLAYER2_ROCK)
    )


def is_draw(player1_shape, player2_shape):
    return (
        (player1_shape == PLAYER1_ROCK and player2_shape == PLAYER2_ROCK)
        or (player1_shape == PLAYER1_PAPER and player2_shape == PLAYER2_PAPER)
        or (player1_shape == PLAYER1_SCISSORS and player2_shape == PLAYER2_SCISSORS)
    )


def generate_rounds():
    for line in generate_input_lines():
        player1_shape, player2_shape = line.split()
        yield player1_shape, player2_shape


def generate_input_lines():
    with open("input.txt", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
