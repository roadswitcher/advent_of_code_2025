"""Day 9 AOC 2025"""
import csv
from itertools import combinations


def area_of_rect(corner_1, corner_2):
    """Given two corners, return the INCLUSIVE area of the rectangle"""
    return (abs(corner_1[0] - corner_2[0]) + 1) * (abs(corner_1[1] - corner_2[1]) + 1)

def line_crosses_rect(p1, p2, corner1, corner2):
    """Returns True if line segment crosses THROUGH the rectangle interior"""
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    # Use the RECTANGLE's boundaries
    min_x = min(corner1[0], corner2[0]) + 1
    max_x = max(corner1[0], corner2[0]) - 1
    min_y = min(corner1[1], corner2[1]) + 1
    max_y = max(corner1[1], corner2[1]) - 1

    # Parametric clipping parameters (Liang-Barsky)
    p = [-dx, dx, -dy, dy]
    q = [x1 - min_x, max_x - x1, y1 - min_y, max_y - y1]
    
    t_enter = 0.0
    t_exit = 1.0

    for i in range(4):
        if p[i] == 0:  # Line is parallel to this boundary
            if q[i] < 0:
                return False  # Parallel and outside
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                t_enter = max(t_enter, t)
            else:
                t_exit = min(t_exit, t)

    # Line crosses if it enters and exits the rectangle at interior points
    return t_enter <= t_exit and 0 < t_enter < 1 and 0 < t_exit < 1

def point_in_polygon(point, coords):
    """Ray casting algorithm to check if point is inside polygon"""
    x, y = point
    n = len(coords)
    inside = False
    
    p1x, p1y = coords[0]
    for i in range(1, n + 1):
        p2x, p2y = coords[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside

def rect_in_polygon(corner1, corner2, coords):
    """Returns True if rectangle is entirely inside the polygon"""
    # Check if ANY polygon edge crosses through the rectangle
    for i in range(len(coords)):
        p1 = coords[i]
        p2 = coords[(i + 1) % len(coords)]
        
        if line_crosses_rect(p1, p2, corner1, corner2):
            return False  # Rectangle extends outside polygon
    
    # Also check that the center of the rectangle is inside the polygon
    center_x = (corner1[0] + corner2[0]) / 2
    center_y = (corner1[1] + corner2[1]) / 2
    
    if not point_in_polygon([center_x, center_y], coords):
        return False
    
    return True  # No edges cross through and center is inside

def pt1_biggest_area(coords):
    """Given a list of coordinates, return the area of the biggest rectangle"""
    area = 0
    for p1, p2 in combinations(coords,2):
        area = max(area_of_rect(p1,p2), area)
    return area

def pt2_biggest_area(coords):
    """Given a list of coordinates, return the area of the biggest rectangle completely contained
    within the outer coordinates."""
    n_pts = len(coords)
    rect_list = []

    for corner1, corner2 in combinations(coords,2):
        rect_area = area_of_rect(corner1, corner2)
        in_polygon = rect_in_polygon(corner1, corner2, coords)
        print(rect_area, corner1, corner2, in_polygon)
        if(in_polygon):
            rect_list.append([rect_area, [corner1, corner2]])

    rect_list.sort(key=lambda x: x[0], reverse=True)
    print(rect_list)
    return rect_list[0][0]


if __name__ == '__main__':
    filename = "test_input.txt"
    # filename = "input.txt"

    list_of_coords = []
    with open(filename) as csvfile:
        list_of_coords = [list(map(int, row)) for row in csv.reader(csvfile)]

    # print(list_of_coords)
    print(f" Part 1: {pt1_biggest_area(list_of_coords)}")

    print(f" Part 2: {pt2_biggest_area(list_of_coords)}")