from os.path import dirname, join


def read_tree_grid():
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        return [[int(x) for x in line.strip()] for line in f]


def print_grid(grid):
    for line in grid:
        print("".join([str(x) for x in line]))
