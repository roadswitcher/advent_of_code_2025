"""Day 4 AOC 2025"""


def read_input(filename: str) -> list:
    """Read input from file"""
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def number_of_neighbors(row: int, col: int, grid: list, occupied_space="@") -> int:
    """Return number of neighbors for a cell in grid"""
    rows = len(grid)
    cols = len(grid[0])

    count = 0
    # Iterate over neighbor offsets
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue

            nr = row + dr
            nc = col + dc

            # bounds-check
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == occupied_space:
                    count += 1

    return count


def pt1_cell_count(grid) -> None:
    """Print number of cells with fewer than 4 neighbors"""
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if (
                grid[row][col] == "@"
                and number_of_neighbors(row, col, grid, occupied_space="@") < 4
            ):
                count += 1
    print(count)


def pt2_how_many_rolls(grid) -> None:
    """Number of rolls total that can be removed"""
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    not_done = True

    while not_done:
        grid_two = []
        prev_count = count
        for row in range(rows):
            new_row = ""
            for col in range(cols):
                if (
                    grid[row][col] == "@"
                    and number_of_neighbors(row, col, grid, occupied_space="@") < 4
                ):
                    new_row += "."  # Replace with empty
                    count += 1
                else:
                    new_row += grid[row][col]
            grid_two.append(new_row)

        grid = grid_two

        if count == prev_count:
            not_done = False
    print(count)


if __name__ == "__main__":
    # filename = "test_input.txt"
    filename = "input.txt"
    warehouse_grid = read_input(filename)
    # print(warehouse_grid)
    pt1_cell_count(warehouse_grid)
    pt2_how_many_rolls(warehouse_grid)
