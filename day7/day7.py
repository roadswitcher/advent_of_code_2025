"""Day 7, AOC 2025"""
from tqdm import tqdm

def read_input(filename: str) -> list:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def print_tree(rows):
    for row in rows:
        print(row)

def pt1_count_splits(rows):
    beam = '|'
    splitter = '^'
    beams_visualized = []
    split_count = 0
    # find where it starts, first row
    startpos = rows[0].index('S')
    beams_visualized.append(rows[0])
    entry_row = list(rows[1])
    entry_row[startpos]=beam
    beams_visualized.append("".join(entry_row))

    # Process remaining rows
    for row_id in tqdm(range(2, len(rows))):
        # Find beams from previous 
        prev_row = beams_visualized[row_id - 1]
        incoming_beams = [idx for idx, char in enumerate(prev_row) if char == beam]
        # Find splitters in current row
        new_row = list(rows[row_id])
        for beam_idx in incoming_beams:
            if new_row[beam_idx] == splitter:
                new_row[beam_idx-1] = beam
                new_row[beam_idx+1] = beam
                split_count += 1
            else:
                new_row[beam_idx] = beam
        new_row = "".join(new_row)
        beams_visualized.append(new_row)

    return split_count, beams_visualized
        


if __name__ == '__main__':
    filename = "test_input.txt"
    filename = "input.txt"

    raw_data = read_input(filename)

    split_count, beams_in_tree = pt1_count_splits(raw_data)

    print(f'Pt 1: Split count = {split_count}')

    # print_tree(beams_in_tree)