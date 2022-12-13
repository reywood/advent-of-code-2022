from common import Directory, create_directory_tree, print_directory_tree


def main():
    root = create_directory_tree()

    print_directory_tree(root)

    print(get_sum_of_sizes_of_directories_under_value(root, 100_000))


def get_sum_of_sizes_of_directories_under_value(
    directory: Directory, max_size: int
) -> int:
    size_sum = 0
    if directory.get_size() <= max_size:
        size_sum = directory.get_size()

    for subdir in directory.subdirectories:
        size_sum += get_sum_of_sizes_of_directories_under_value(subdir, max_size)

    return size_sum


if __name__ == "__main__":
    main()
