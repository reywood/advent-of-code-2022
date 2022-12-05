from typing import Generator, Tuple, Set
from os.path import dirname, join


def main():
    matching_item_priorities = list(generate_matching_item_priorities())

    print(matching_item_priorities)
    print(sum(matching_item_priorities))


def generate_matching_item_priorities():
    for compartment1, compartment2 in generate_unique_rucksack_contents():
        same = compartment1.intersection(compartment2)
        if same:
            for item in same:
                yield get_item_priority(item)


def generate_unique_rucksack_contents() -> Generator[Tuple[Set, Set]]:
    for line in generate_input_lines():
        yield set(line[: len(line) // 2]), set(line[len(line) // 2 :])


def generate_input_lines() -> Generator[str]:
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip()


def get_item_priority(item) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1

    if item.isupper():
        return ord(item) - ord("A") + 27


if __name__ == "__main__":
    main()
