"""Day 9 AOC 2025"""
import csv


def area_of_rect(corner_1, corner_2):
    """Given two corners, return the INCLUSIVE area of the rectangle"""
    return (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)


def pt1_biggest_area(coords):
    """Given a list of coordinates, return the area of the biggest area"""
    area = 0
    for i, coord in enumerate(coords):
        rest = coords[:i] + coords[i + 1:]
        for corner_two in rest:
            area = max(area, area_of_rect(coord, corner_two))
    return area


if __name__ == '__main__':
    filename = "test_input.txt"
    # filename = "input.txt"

    list_of_coords = []
    with open(filename) as csvfile:
        list_of_coords = [tuple(map(int, row)) for row in csv.reader(csvfile)]

    # print(list_of_coords)
    print(f" Part 1: {pt1_biggest_area(list_of_coords)}")
