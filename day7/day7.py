"""Day 7, AOC 2025"""

def read_input(filename: str) -> list:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def print_tree(rows):
    for row in rows:
        print(row)

def pt1_count_splits(rows):
    count = 0
    beams_visualized = []
    # find where it starts, first row
    startpos = rows[0].index('S')
    beams_visualized.append(rows[0])
    for
if __name__ == '__main__':
    filename = "test_input.txt"

    raw_data = read_input(filename)

    print_tree(raw_data)