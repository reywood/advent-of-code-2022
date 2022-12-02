POINTS_FOR_WIN = 6
POINTS_FOR_DRAW = 3
POINTS_FOR_LOSS = 0

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

PLAYER1_SHAPE_MAP = {"A": ROCK, "B": PAPER, "C": SCISSORS}
PLAYER2_SHAPE_MAP = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

SHAPE_POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
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
        (player1_shape == ROCK and player2_shape == PAPER)
        or (player1_shape == PAPER and player2_shape == SCISSORS)
        or (player1_shape == SCISSORS and player2_shape == ROCK)
    )


def is_draw(player1_shape, player2_shape):
    return player1_shape == player2_shape


def generate_rounds():
    for line in generate_input_lines():
        player1_shape, player2_shape = line.split()
        yield PLAYER1_SHAPE_MAP[player1_shape], PLAYER2_SHAPE_MAP[player2_shape]


def generate_input_lines():
    with open("input.txt", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
