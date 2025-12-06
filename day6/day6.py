"""Day 6, AOC 2025"""

import pandas as pd
from itertools import groupby
from math import prod


def pt1_operation_on_columns(df):
    """Treat DF as a giant RPN problem-- sum() or prod() each column, and sum results"""
    accumulator = 0

    for column in df.columns:
        accumulator += df[column][:-1].astype(int).prod() \
            if df[column].iloc[-1] != '+' \
            else df[column][:-1].astype(int).sum()
    return accumulator


def pt2_cephalopod_total(rows):
    """Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most
    significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a
    column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)"""
    height = len(rows)
    total = 0
    # Transpose to match problem statement
    transposed_rows = [''.join(col) for col in zip(*rows)]

    # Group into problems, dropping the blank lines
    problems = [list(g) for k, g in groupby(transposed_rows, key=lambda c: bool(c.strip())) if k]
    for problem in problems:
        op = problem[0][-1]
        problem[0] = problem[0][:-1]
        nums = [int(num) for num in problem]
        total += prod(nums) if op == '*' else sum(nums)

    return total


if __name__ == "__main__":
    # filename = "test_input.txt"
    filename = "input.txt"

    df = pd.read_csv(filename, sep='\\s+', header=None)
    print(f" Part 1 {pt1_operation_on_columns(df)}")

    with open(filename) as f:
        datalist_without_newlines = [line.rstrip('\n') for line in f]

    # print(datalist_without_newlines)
    print(f" Part 2 {pt2_cephalopod_total(datalist_without_newlines)}")
