from common import perform_all_moves


def main():
    knot_positions = [(0, 0) for _ in range(10)]
    positions_visited = set([knot_positions[-1]])

    perform_all_moves(knot_positions, positions_visited)

    print(len(positions_visited))


if __name__ == "__main__":
    main()
