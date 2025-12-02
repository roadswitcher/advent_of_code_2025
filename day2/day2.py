"""Day 2, AOC 2025"""


def is_bad_id(number: int) -> bool:
    """Given a number, return whether it is a bad id by checking if it is made of repeating digits per
    the instructions"""
    # odd length fails by default
    if len(str(number)) % 2 != 0:
        return False
    half = len(str(number)) // 2
    return str(number)[half:] == str(number)[:half]


def find_bad_ids(low: int, high: int) -> list:
    """Yield all numbers in [low, high] that satisfy is_bad_id()."""
    for n in range(low, high + 1):
        if is_bad_id(n):
            yield n


def find_bad_ids_pt2(low: int, high: int) -> list:
    """Yield all numbers in [low, high] that satisfy is_bad_id()."""
    for n in range(low, high + 1):
        if is_bad_id_pt2(n):
            yield n


def is_bad_id_pt2(n: int) -> bool:
    """string trick"""
    s = str(n)
    return s in (s + s)[1:-1]


def parse_id_range(range: str) -> tuple:
    """Given a string with two numbers separated by a dash, return a tuple"""
    low, high = map(int, range.split("-"))
    return low, high


def sum_bad_ids(id_ranges: list[str]) -> int:
    total = 0
    for rng in id_ranges:
        low, high = parse_id_range(rng)
        total += sum(find_bad_ids(low, high))
    return total


def sum_bad_ids_pt2(id_ranges: list[str]) -> int:
    total = 0
    for rng in id_ranges:
        low, high = parse_id_range(rng)
        total += sum(find_bad_ids_pt2(low, high))
    return total


if __name__ == "__main__":
    with open("input.txt") as input_file:
        single_line = input_file.readline().strip()
        data_list = single_line.split(",")
    print(data_list)
    print(sum_bad_ids(data_list))
    print(sum_bad_ids_pt2(data_list))
