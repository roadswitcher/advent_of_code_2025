"""Day 9 AOC 2025"""
import csv
from itertools import combinations

def area_of_rect(corner_1, corner_2):
    """Given two corners, return the INCLUSIVE area of the rectangle"""
    return (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)

def yield_rect_coords(p1, p2):
    """Yields all integer coordinates within the rectangle."""
    x_min, x_max = sorted([p1[0], p2[0]])
    y_min, y_max = sorted([p1[1], p2[1]])
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            yield [x, y]

def is_on_edge(point, p1, p2):
    """Checks if a point lies exactly on the segment p1-p2"""
    x, y = point
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 == x: return min(y1, y2) <= y <= max(y1, y2)
    if y1 == y2 == y: return min(x1, x2) <= x <= max(x1, x2)

    if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
        return (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1)
    return False

def point_in_polygon(point, coords):
    """Ray casting algorithm + boundary check"""
    # 1. Explicitly check if the point is on the boundary
    n = len(coords)
    for i in range(n):
        if is_on_edge(point, coords[i], coords[(i + 1) % n]):
            return True

    # 2. Standard Ray Casting
    x, y = point
    inside = False
    p1x, p1y = coords[0]
    for i in range(1, n + 1):
        p2x, p2y = coords[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def is_rect_in_polygon(corner1, corner2, coords):
    """Returns True if every point in the rectangle is inside/on the polygon"""
    for pt in yield_rect_coords(corner1, corner2):
        if not point_in_polygon(pt, coords):
            return False
    return True
    
def pt1_biggest_area(coords):
    """Area of the biggest rectangle formed by any two provided corners"""
    return max((area_of_rect(p1, p2) for p1, p2 in combinations(coords, 2)), default=0)

def pt2_biggest_area(coords):
    """Area of the biggest rectangle formed by two corners that is fully contained"""
    max_area = 0
    for corner1, corner2 in combinations(coords, 2):
        # Don't run the expensive raycast if the area is already smaller
        current_area = area_of_rect(corner1, corner2)
        if current_area > max_area:
            if is_rect_in_polygon(corner1, corner2, coords):
                max_area = current_area
    return max_area


if __name__ == '__main__':
    # filename = "test_input.txt"
    filename = "input.txt"

    list_of_coords = []
    with open(filename) as csvfile:
        list_of_coords = [list(map(int, row)) for row in csv.reader(csvfile)]

    # print(list_of_coords)
    print(f" Part 1: {pt1_biggest_area(list_of_coords)}")

    print(f" Part 2: {pt2_biggest_area(list_of_coords)}")