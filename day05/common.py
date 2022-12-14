import re
from os.path import dirname, join
from typing import Any, Generator, List, Tuple


class Move:
    def __init__(self, count, from_stack, to_stack):
        self.count = count
        self.from_stack = from_stack
        self.to_stack = to_stack

    def __repr__(self):
        return f"Move({self.count}, {self.from_stack}, {self.to_stack})"


class CrateStacks:
    def __init__(self):
        self.stacks = []

    def add_layer(self, layer):
        self._ensure_stack_count(len(layer))

        for column, crate in enumerate(layer):
            if crate is not None:
                self.stacks[column].insert(0, crate)

    def remove_crates_from_stack(self, stack, count):
        removed_crates = self.stacks[stack - 1][-count:]
        self.stacks[stack - 1] = self.stacks[stack - 1][:-count]
        return removed_crates

    def add_crates_to_stack(self, stack, crates):
        self.stacks[stack - 1].extend(crates)

    def _ensure_stack_count(self, count):
        for _ in range(count - len(self.stacks)):
            self.stacks.append([])


def read_stacks_and_moves() -> Tuple[CrateStacks, List[Move]]:
    line_generator = generate_input_lines()

    crate_stacks = read_crate_stacks(line_generator)
    moves = read_moves(line_generator)

    return crate_stacks, moves


def read_crate_stacks(line_generator) -> CrateStacks:
    crate_stacks = CrateStacks()
    for line in line_generator:
        if does_line_contain_crates(line):
            crate_layer = parse_crate_layer(line)
            crate_stacks.add_layer(crate_layer)
        else:
            break

    return crate_stacks


def read_moves(line_generator) -> List[Move]:
    return [parse_move(line) for line in line_generator if does_line_contain_move(line)]


def does_line_contain_crates(line) -> bool:
    match = re.match(r".*\[[A-Z]\]", line)
    return match is not None


def parse_crate_layer(line) -> List[str]:
    line += " "
    crate_stack_char_count = 4
    number_of_stacks = len(line) // crate_stack_char_count
    crate_stack_layer = [None] * number_of_stacks

    for column_index in range(number_of_stacks):
        str_index = column_index * crate_stack_char_count
        if line[str_index] == "[":
            crate_stack_layer[column_index] = line[str_index + 1]

    return crate_stack_layer


def does_line_contain_move(line: str) -> bool:
    return line.startswith("move ") and " from " in line and " to " in line


def parse_move(line) -> Move:
    match = re.match(r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)$", line)
    return Move(int(match.group(1)), int(match.group(2)), int(match.group(3)))


def generate_input_lines() -> Generator[str, Any, Any]:
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip("\n")
