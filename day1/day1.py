"""
Day 1, Advent of Code
"""

from pathlib import Path


def compute_dial_position(position, direction, steps, total_positions=100):
    """Computes the new position on a combination dial."""
    delta = steps if direction == "L" else -steps
    return (position + delta) % total_positions


def count_zero_crossings(start, steps, direction, total_positions=100):
    """Count how many times we click through zero."""
    delta = 1 if direction == "L" else -1
    return sum((start + delta * i) % total_positions == 0 for i in range(1, steps + 1))


def solve_combination_lock(instructions, count_crossings=False, total_positions=100):
    """Solve the combination lock puzzle.

    Args:
        instructions: List of direction+steps strings (e.g., ['L68', 'R30'])
        count_crossings: If True, count all passes through zero.
                        If False, only count when landing on zero.
    """
    position = 50
    password = 0

    for instruction in instructions:
        direction, steps = instruction[0], int(instruction[1:])

        if count_crossings:
            password += count_zero_crossings(
                position, steps, direction, total_positions
            )

        position = compute_dial_position(position, direction, steps, total_positions)

        if not count_crossings and position == 0:
            password += 1

    return password


def read_input(filename: Path) -> str:
    """Given a set of combination instructions, read the input file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


if __name__ == "__main__":
    # pt1 = solve_combination_lock(read_input(Path('test_input.txt')), count_crossings=False)
    # pt2 = solve_combination_lock(read_input(Path('test_input.txt')), count_crossings=True)
    # print(f'Part 1: {pt1}, Part 2: {pt2}')
    pt1 = solve_combination_lock(read_input(Path("input.txt")), count_crossings=False)
    pt2 = solve_combination_lock(read_input(Path("input.txt")), count_crossings=True)
    print(f"Part 1: {pt1}, Part 2: {pt2}")
