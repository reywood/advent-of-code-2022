import re
from abc import ABC, abstractmethod
from itertools import chain
from os.path import dirname, join
from typing import Any, Generator


class Node(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass


class Directory(Node):
    def __init__(self, name: str, parent: "Directory" = None):
        self.name = name
        self.parent = parent or self
        self.files = []
        self.subdirectories = []

    def get_subdirectory(self, name: str):
        for subdir in self.subdirectories:
            if subdir.name == name:
                return subdir

        return self.create_subdirectory(name)

    def create_subdirectory(self, name: str) -> "Directory":
        subdirectory = Directory(name, self)
        self.subdirectories.append(subdirectory)
        return subdirectory

    def create_file(self, name: str, size: int):
        file = File(name, size)
        self.files.append(file)
        return file

    def get_size(self) -> int:
        return sum(node.get_size() for node in chain(self.files, self.subdirectories))


class File(Node):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size


class DirectoryCommand(ABC):
    @abstractmethod
    def execute(self, current_directory: Directory) -> Directory:
        # This method should return the directory that the command ends up in
        pass


class ChangeDirCommand(DirectoryCommand):
    def __init__(self, dir_name: str):
        self.dir_name = dir_name

    def execute(self, current_directory: Directory) -> Directory:
        if self.dir_name == "..":
            return current_directory.parent

        return current_directory.get_subdirectory(self.dir_name)


class ListCommand(DirectoryCommand):
    def __init__(self):
        self.file_names_and_sizes = []
        self.directory_names = []

    def add_file(self, name: str, size: int):
        self.file_names_and_sizes.append((name, size))

    def add_directory(self, name: str):
        self.directory_names.append(name)

    def execute(self, current_directory: Directory) -> Directory:
        for dir_name in self.directory_names:
            current_directory.create_subdirectory(dir_name)

        for file_name, size in self.file_names_and_sizes:
            current_directory.create_file(file_name, size)

        return current_directory


def create_directory_tree() -> Directory:
    root = Directory("")
    current_directory = root

    for command in generate_commands():
        current_directory = command.execute(current_directory)

    return root


def print_directory_tree(directory: Directory, indent=0):
    print(f"{'  ' * indent}- {directory.name} (dir) {directory.get_size()}")
    for subdir in directory.subdirectories:
        print_directory_tree(subdir, indent + 1)
    for file in directory.files:
        print(f"{'  ' * (indent + 1)}- {file.name} {file.size}")


def generate_commands():
    current_list_command = None
    for line in generate_input_lines():
        if line.startswith("$") and current_list_command:
            yield current_list_command
            current_list_command = None

        if line.startswith("$ cd "):
            yield create_cd_command(line)

        elif line == "$ ls":
            current_list_command = ListCommand()

        else:
            add_node_to_list_command(current_list_command, line)

    if current_list_command:
        yield current_list_command


def create_cd_command(line) -> ChangeDirCommand:
    dir_name = line[len("$ cd ") :]
    return ChangeDirCommand(dir_name)


def add_node_to_list_command(list_command: ListCommand, line: str):
    dir_prefix = "dir "
    if line.startswith(dir_prefix):
        list_command.add_directory(line[len(dir_prefix) :])

    else:
        match = re.match(r"^(?P<size>[0-9]+) (?P<name>.+)$", line)
        if match:
            list_command.add_file(match.group("name"), int(match.group("size")))
        else:
            raise Exception(f"Unknown list output line format: {line}")


def generate_input_lines() -> Generator[str, Any, Any]:
    with open(join(dirname(__file__), "input.txt"), "r") as f:
        for line in f:
            yield line.strip("\n")
