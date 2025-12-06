"""Day 5, AOC 2025"""

from typing import List


def merge_ranges(ranges: List) -> List:
    """Merge overlapping ranges"""
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    current_start, current_end = sorted_ranges[0]
    for new_start, new_end in sorted_ranges[1:]:
        if new_start <= current_end:
            current_end = max(current_end, new_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = new_start, new_end

    merged.append((current_start, current_end))
    return merged


def is_item_fresh(item: int, fresh_ranges: List) -> List:
    """Return true if item is in a range, thus fresh"""
    for range in fresh_ranges:
        if range[0] <= item <= range[1]:
            return True
    return False


def pt1(ranges, ids):
    fresh_count = 0
    for item in ids:
        if is_item_fresh(item, ranges):
            print(f"{item} is fresh")
            fresh_count += 1
        else:
            print(f"{item} is not fresh")

    print(f"{fresh_count} fresh items are fresh")


def pt2(ranges):
    """how many ids are fresh"""
    fresh_count = 0
    for range in ranges:
        fresh_count += range[1] - range[0] + 1

    print(f" There are {fresh_count} ids for fresh")


def read_data(filename: str):
    ranges = []
    ids = []

    filecontents = (line.rstrip("\r\n") for line in open(filename))
    for line in filecontents:
        if "-" in line:
            low, high = line.split("-")
            ranges.append((int(low), int(high)))
        elif line != "":
            ids.append(int(line))

    return ranges, ids


if __name__ == "__main__":
    ranges, ids = read_data("input.txt")
    ranges = merge_ranges(ranges)

    pt1(ranges, ids)
    pt2(ranges)
