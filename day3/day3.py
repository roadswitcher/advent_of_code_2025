"""Day 3, AOC 2025"""


def idx_leftmost_max(bank: str) -> int:
    """Return the index of the maximum digit in first N-1 digits of number string of length N"""
    bank = [int(batt) for batt in bank]
    max_num = max(bank)
    return bank.index(max_num)


def bank_largest_joltage_n(bank: str, n: int) -> int:
    """Return the largest N-digit joltage available in bank
    """
    if len(bank) < n + 1:
        raise ValueError("Bank must be at least N+1 characters")

    tot = 0
    pos = 0

    for picked_so_far in range(n):
        # how many digits we still need AFTER this pick
        remaining_cells_needed = n - 1 - picked_so_far
        search_end = len(bank) - remaining_cells_needed

        # find leftmost max in the current window
        rel = idx_leftmost_max(bank[pos:search_end])
        pos += rel

        tot = tot * 10 + int(bank[pos])
        pos += 1

    return tot


def joltages(battery_banks: list, num_cells: int) -> int:
    """Given a list of strings representing battery banks, return the joltage available with N cells"""
    joltage = 0
    for bank in battery_banks:
        joltage += bank_largest_joltage_n(bank, num_cells)
    return joltage


def read_input(filename: str) -> list:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


if __name__ == '__main__':
    # input_lines = read_input('test_input.txt')
    input_lines = read_input('input.txt')
    # pt 1
    print(joltages(input_lines, 2))
    # pt 2
    print(joltages(input_lines, 12))
