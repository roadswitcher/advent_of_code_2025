"""Day 3, AOC 2025"""

import pathlib
import sys


def digitparse(bank: str) -> list:
    """Parse a battery bank string into a list of digits"""
    return [int(batt) for batt in bank]


def idx_leftmost_max(bank: str) -> int:
    """Return the index of the maximum digit in first N-1 digits of number string of length N"""
    bank = digitparse(bank)
    max_num = max(bank)
    return bank.index(max_num)


def bank_largest_joltage(bank:str) -> int:
    """Given a string representing a battery bank, return the largest joltage available"""
    first_max = idx_leftmost_max(bank[:-1])
    second_chunk = bank[first_max + 1:]
    second_max = idx_leftmost_max(second_chunk)
    # print(bank, first_max, bank[first_max], second_chunk[second_max])
    return int(bank[first_max]+second_chunk[second_max])


def pt1_joltages(battery_banks: list) -> None:
    """Given a list of strings representing battery banks, return the joltage available"""
    joltage = 0
    for bank in battery_banks:
        joltage += bank_largest_joltage(bank)
    print(joltage)


def read_input(filename: Path) -> str:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


if __name__ == '__main__':
    # input_lines = read_input('test_input.txt')
    input_lines = read_input('input.txt')
    print(input_lines)
    pt1_joltages(input_lines)
