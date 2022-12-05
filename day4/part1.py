from common import generate_input_lines
from typing import Generator, Any, Tuple


def main():
    result = generate_does_one_assignment_contain_other_assignment()
    print(sum(1 for does_contain in result if does_contain))


def generate_does_one_assignment_contain_other_assignment() -> Generator[
    bool, Any, Any
]:
    for (start1, end1), (start2, end2) in generate_section_assignment_pairs():
        yield (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1)


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


if __name__ == "__main__":
    main()
