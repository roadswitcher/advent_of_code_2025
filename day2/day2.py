"""Day 2, AOC 2025"""

import csv

if __name__ == '__main__':
    with open('test_input.txt') as input_file:
        single_line = input_file.readline().strip()
        data_list = single_line.split(',')
    print(data_list)