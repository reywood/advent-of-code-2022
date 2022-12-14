def main():
    top_three = sorted(list(generate_elf_calorie_totals()))[-3:]
    print(top_three)
    print(sum(top_three))


def generate_elf_calorie_totals():
    for group in generate_elf_calorie_groups():
        yield sum(group)


def generate_elf_calorie_groups():
    group = []

    for line in generate_input_lines():
        if line == "":
            if len(group) > 0:
                yield group
                group = []
        else:
            group.append(int(line))

    if len(group) > 0:
        yield group


def generate_input_lines():
    with open("input.txt", "r") as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    main()
