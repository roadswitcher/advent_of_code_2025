"""
Day 1, Advent of Code
"""

from pathlib import Path


def compute_dial_position(initial_position, direction, steps, total_positions=100, ):
    """
    Computes the new position on a combination dial.
    """
    if direction == 'L':
        # Clockwise movement increases the position
        new_position = (initial_position + steps) % total_positions
    elif direction == 'R':
        # Counter-clockwise movement decreases the position
        # The (expression + total_positions) % total_positions handles
        # negative results from the modulo operation in a standard way
        new_position = (initial_position - steps + total_positions) % total_positions
    else:
        raise ValueError("Direction must be 'L' or 'R'")

    return new_position


def count_zero_crossings(start, steps, direction, total_positions=100):
    """Count how many times we click through zero."""
    count = 0
    for i in range(1, steps + 1):
        if direction == 'L':
            pos = (start + i) % total_positions
        else:
            pos = (start - i + total_positions) % total_positions

        if pos == 0:
            count += 1

    return count


def compute_password_pt1(input: str) -> int:
    """Given a set of combination instructions, compute the number of times
    the dial lands on zero and return that as the true password.

    Dial starts at 50.
    """
    password = 0
    position = 50

    for instruction in input:
        direction = instruction[0]
        increment = int(instruction[1:])
        new_position = compute_dial_position(position, direction, increment)
        # print(instruction, direction, increment, position, new_position)
        position = new_position
        if position == 0:
            password += 1
    return password


def compute_password_pt2(input: str) -> int:
    """Given a set of combination instructions, compute the number of times
    the dial lands on zero and return that as the true password.

    Dial starts at 50.
    """
    password = 0
    position = 50

    for instruction in input:
        direction = instruction[0]
        increment = int(instruction[1:])
        new_position = compute_dial_position(position, direction, increment)
        # print(instruction, direction, increment, position, new_position)
        password += count_zero_crossings(position, increment, direction)
        position = new_position
    return password


def read_input(filename: Path) -> str:
    """Given a set of combination instructions, read the input file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


if __name__ == '__main__':
    # pt1 = compute_password_pt1(read_input(Path('test_input.txt')))
    # pt2 = compute_password_pt2(read_input(Path('test_input.txt')))
    pt1 = compute_password_pt1(read_input(Path('input.txt')))
    pt2 = compute_password_pt2(read_input(Path('input.txt')))
    print(f'Part 1: {pt1}, Part 2: {pt2}')
