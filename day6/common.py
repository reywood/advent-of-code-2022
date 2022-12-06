import os.path


def find_start_of_unique_marker(text: str, marker_length: int) -> int:
    marker = marker_length
    while len(set(text[marker - marker_length : marker])) != marker_length:
        marker += 1
    return marker


def read_file() -> str:
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        return f.read()
