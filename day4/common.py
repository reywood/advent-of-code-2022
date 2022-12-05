from os.path import dirname, join
from typing import Any, Generator, Tuple


def generate_input_lines() -> Generator[str, Any, Any]:
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip()


def generate_section_assignment_pairs() -> Generator[
    Tuple[Tuple[int, int], Tuple[int, int]], Any, Any
]:
    for line in generate_input_lines():
        yield tuple(
            [
                tuple([int(a) for a in assignment.split("-")])
                for assignment in line.split(",")
            ]
        )
