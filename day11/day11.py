"""Day 11 AOC 2025"""

from functools import cache


def pt1(lines: list) -> None:
    """Pt1 solution"""
    nodes = {}
    for line in lines:
        parts = line.split(': ')
        node = parts[0]
        links = parts[1].strip().split(' ')
        nodes[node] = links
    print(nodes)





if __name__ == "__main__":
    filename = "test_input.txt"
    # filename = "input.txt"

    data = open(filename).read()
    links = {f: ts.split() for f,ts in [line.split(": ") for line in data.split("\n")]}
    print(links)
    print(count_paths('you', 'out'))
    # pt1(lines)