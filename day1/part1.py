def main():
    max = 0
    current = 0
    for line in generate_input_lines():
        if line == "":
            if current > max:
                max = current
            current = 0
        else:
            current += int(line)

    if current > max:
        max = current

    print(max)


def generate_input_lines():
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            yield line


if __name__ == "__main__":
    main()
