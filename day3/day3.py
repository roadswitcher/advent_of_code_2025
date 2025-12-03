"""Day 3, AOC 2025"""

import pathlib
import sys

def idx_leftmost_max(number:str) -> int:
    """Return the index of the maximum digit in first N-1 digits of number string of length N"""
    digits = [ int(digit) for digit in number[:-1]]
    max_num = max(digits)
    return digits.index(max_num)

def part1_largest_joltage(battery_banks: list) -> int:
    """Given a list of strings representing battery banks, return the largest joltage available"""
    for bank in battery_banks:
        


def read_input(filename: Path) -> str:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

if __name__ == '__main__':
    input_lines = read_input('test_input.txt')
    print(input_lines)
    for line in input_lines:
        print(f"Line: {line}   Max: {line[idx_leftmost_max(line)]}")
