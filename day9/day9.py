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
    min_x = min(corner1[0], corner2[0])
    max_x = max(corner1[0], corner2[0])
    min_y = min(corner1[1], corner2[1])
    max_y = max(corner1[1], corner2[1])

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

def is_rect_inside_polygon(corner1, corner2, polygon_points):
    """Returns True if rectangle is entirely inside the polygon"""
    # Check if ANY polygon edge crosses through the rectangle
    for i in range(len(polygon_points)):
        p1 = polygon_points[i]
        p2 = polygon_points[(i + 1) % len(polygon_points)]
        
        if line_crosses_rect(p1, p2, corner1, corner2):
            return False  # Rectangle extends outside polygon
    
    return True


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
        rect_list.append([rect_area, [corner1, corner2]])

    rect_list.sort(key=lambda x: x[0], reverse=True)

    for rect in rect_list:
        intersection_found = False
        rect_area = rect[0]
        corner1 = rect[1][0]
        corner2 = rect[1][1]
        
        for i in range(n_pts):
            p1 = coords[i]
            p2 = coords[(i+1)%n_pts]
            intersection = line_crosses_rect(p1, p2, corner1, corner2)
            intersection_found = intersection_found or intersection


            print(f'rect area {rect_area} corners: {corner1, corner2} points {p1, p2} intersection found? {intersection_found}')


    rect_list.sort(key=lambda x: x[0], reverse=True)

    return rect_list[0]


if __name__ == '__main__':
    filename = "test_input.txt"
    # filename = "input.txt"

    list_of_coords = []
    with open(filename) as csvfile:
        list_of_coords = [list(map(int, row)) for row in csv.reader(csvfile)]

    # print(list_of_coords)
    # print(f" Part 1: {pt1_biggest_area(list_of_coords)}")

    print(f" Part 2: {pt2_biggest_area(list_of_coords)}")