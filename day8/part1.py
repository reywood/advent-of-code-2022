from common import read_tree_grid


def main():
    tree_grid = read_tree_grid()

    number_of_visible_trees = sum(
        1
        for y in range(len(tree_grid))
        for x in range(len(tree_grid[y]))
        if is_tree_visible(tree_grid, x, y)
    )

    print(number_of_visible_trees)


def is_tree_visible(grid, x, y) -> bool:
    return (
        is_tree_visible_from_left(grid, x, y)
        or is_tree_visible_from_right(grid, x, y)
        or is_tree_visible_from_above(grid, x, y)
        or is_tree_visible_from_below(grid, x, y)
    )


def print_grid(grid):
    for line in grid:
        print("".join(line))


def is_tree_visible_from_left(grid, x, y) -> bool:
    return all(grid[y][xleft] < grid[y][x] for xleft in range(x))


def is_tree_visible_from_right(grid, x, y) -> bool:
    return all(grid[y][xright] < grid[y][x] for xright in range(x + 1, len(grid[y])))


def is_tree_visible_from_above(grid, x, y) -> bool:
    return all(grid[ytop][x] < grid[y][x] for ytop in range(y))


def is_tree_visible_from_below(grid, x, y) -> bool:
    return all(grid[ybottom][x] < grid[y][x] for ybottom in range(y + 1, len(grid)))


if __name__ == "__main__":
    main()
