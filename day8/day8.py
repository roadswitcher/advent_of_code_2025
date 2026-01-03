"""Day 8, AOC 2025"""
import math
from copy import deepcopy

def read_data(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    data = [[int(coord.strip()) for coord in box.split(',')] for box in lines]
    return data

def distance_between_boxes(box1, box2):
    return math.dist(box1, box2)

def closest_boxes(boxes):
    closest_pairs = []
    for i, box in enumerate(boxes):
        


if __name__=="__main__":
    filename = "test_input.txt"

    boxes = read_data(filename)
    print(boxes)
