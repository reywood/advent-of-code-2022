from os.path import dirname, join
from typing import Generator, Any


def generate_input_lines() -> Generator[str, Any, Any]:
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip()


def get_item_priority(item) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1

    if item.isupper():
        return ord(item) - ord("A") + 27
