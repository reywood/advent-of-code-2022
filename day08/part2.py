from common import read_tree_grid


def main():
    tree_grid = read_tree_grid()

    max_scenic_score = max(
        calculate_scenic_score(tree_grid, x, y)
        for y in range(len(tree_grid))
        for x in range(len(tree_grid[y]))
    )

    print(max_scenic_score)


def calculate_scenic_score(grid, x, y) -> int:
    return (
        get_view_distance_left(grid, x, y)
        * get_view_distance_right(grid, x, y)
        * get_view_distance_above(grid, x, y)
        * get_view_distance_below(grid, x, y)
    )


def get_view_distance_left(grid, x, y) -> int:
    return get_view_distance(
        grid[y][x],
        range(x - 1, -1, -1),
        lambda xleft: grid[y][xleft],
    )


def get_view_distance_right(grid, x, y) -> int:
    return get_view_distance(
        grid[y][x],
        range(x + 1, len(grid[y])),
        lambda xright: grid[y][xright],
    )


def get_view_distance_above(grid, x, y) -> int:
    return get_view_distance(
        grid[y][x],
        range(y - 1, -1, -1),
        lambda ytop: grid[ytop][x],
    )


def get_view_distance_below(grid, x, y) -> int:
    return get_view_distance(
        grid[y][x],
        range(y + 1, len(grid)),
        lambda ybottom: grid[ybottom][x],
    )


def get_view_distance(tree_height, range_to_look_at, tree_finder) -> int:
    view_distance = 0
    for position in range_to_look_at:
        view_distance += 1
        if tree_finder(position) >= tree_height:
            break
    return view_distance


if __name__ == "__main__":
    main()
