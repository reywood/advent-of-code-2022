from common import Directory, create_directory_tree


def main():
    total_file_space = 70_000_000
    space_required_for_update = 30_000_000

    root = create_directory_tree()

    space_currently_in_use = root.get_size()
    space_current_unused = total_file_space - space_currently_in_use
    remaining_space_needed_for_update = space_required_for_update - space_current_unused

    possible_sizes_to_delete = find_sizes_of_eligible_directories(
        root, remaining_space_needed_for_update
    )

    print(sorted(possible_sizes_to_delete)[0])


def find_sizes_of_eligible_directories(root: Directory, min_size: int):
    possible_sizes_to_delete = []
    directories_to_traverse = [root]

    while len(directories_to_traverse) > 0:
        current_dir = directories_to_traverse.pop()
        directories_to_traverse.extend(current_dir.subdirectories)
        if current_dir.get_size() >= min_size:
            possible_sizes_to_delete.append(current_dir.get_size())

    return possible_sizes_to_delete


if __name__ == "__main__":
    main()
