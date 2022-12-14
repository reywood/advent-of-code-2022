from common import find_start_of_unique_marker, read_file


def main():
    contents = read_file()
    print(find_start_of_message_marker(contents))


def find_start_of_message_marker(text: str) -> int:
    return find_start_of_unique_marker(text, 14)


if __name__ == "__main__":
    main()
