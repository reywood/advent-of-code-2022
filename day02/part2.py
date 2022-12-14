from os.path import dirname, join

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSS = "X"
DRAW = "Y"
WIN = "Z"

SHAPE_POINTS = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

OUTCOME_POINTS = {
    LOSS: 0,
    DRAW: 3,
    WIN: 6,
}

DESIRED_OUTCOME_MAP = {
    LOSS: {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER,
    },
    WIN: {
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK,
    },
}


def main():
    player2_points_per_round = [
        calculate_player2_points_for_round(player1_shape, desired_outcome)
        for player1_shape, desired_outcome in generate_rounds()
    ]

    print(player2_points_per_round)
    print(sum(player2_points_per_round))


def calculate_player2_points_for_round(player1_shape, desired_outcome):
    player2_shape = determine_desired_player2_shape(player1_shape, desired_outcome)
    return OUTCOME_POINTS[desired_outcome] + SHAPE_POINTS[player2_shape]


def determine_desired_player2_shape(player1_shape, desired_outcome):
    if desired_outcome == DRAW:
        return player1_shape

    return DESIRED_OUTCOME_MAP[desired_outcome][player1_shape]


def generate_rounds():
    for line in generate_input_lines():
        player1_shape, desired_outcome = line.split()
        yield player1_shape, desired_outcome


def generate_input_lines():
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
