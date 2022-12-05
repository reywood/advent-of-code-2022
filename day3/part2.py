from common import generate_input_lines, get_item_priority


def main():
    badges = list(generate_badges())
    print(badges)
    print(sum(get_item_priority(badge) for badge in badges))


def generate_badges():
    for elf1, elf2, elf3 in generate_elf_groups():
        yield elf1.intersection(elf2).intersection(elf3).pop()


def generate_elf_groups():
    results = generate_unique_rucksack_contents()
    try:
        while True:
            yield (
                next(results),
                next(results),
                next(results),
            )
    except StopIteration:
        pass

    # for contents in generate_unique_rucksack_contents():


def generate_unique_rucksack_contents():
    for line in generate_input_lines():
        yield set(line)


if __name__ == "__main__":
    main()
