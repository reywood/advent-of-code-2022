from typing import Any, Generator

from common import generate_section_assignment_pairs


def main():
    result = generate_does_one_assignment_contain_other_assignment()
    print(sum(1 for does_contain in result if does_contain))


def generate_does_one_assignment_contain_other_assignment() -> Generator[
    bool, Any, Any
]:
    for (start1, end1), (start2, end2) in generate_section_assignment_pairs():
        yield (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1)


if __name__ == "__main__":
    main()
