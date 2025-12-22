import csv
from itertools import combinations, product
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

# We must keep this global or outside solve() for the workers to access it
def check_point_worker(args):
    """Worker function for parallel mapping"""
    point, poly_coords = args
    if point_in_polygon(point, poly_coords):
        return point
    return None

def point_in_polygon(point, coords):
    x, y = point
    n = len(coords)
    inside = False
    p1x, p1y = coords[0]
    for i in range(1, n + 1):
        p2x, p2y = coords[i % n]
        if p1x == p2x == x and min(p1y, p2y) <= y <= max(p1y, p2y): return True
        if p1y == p2y == y and min(p1x, p2x) <= x <= max(p1x, p2x): return True
        if y > min(p1y, p2y) and y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def solve():
    with open("input.txt") as f:
        poly_coords = [list(map(int, row)) for row in csv.reader(f)]

    # Part 1
    p1_area = max(get_area(c1, c2) for c1, c2 in combinations(poly_coords, 2))
    print(f"Part 1: {p1_area}")

    # Part 2 Setup
    all_x = [c[0] for c in poly_coords]
    all_y = [c[1] for c in poly_coords]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    total_cells = (max_x - min_x + 1) * (max_y - min_y + 1)
    
    custom_bar = "{desc}: {percentage:3.0f}% |{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"

    # --- Parallel Grid Mapping ---
    valid_points = set()
    print(f"Mapping {total_cells} grid cells using parallel processes...")
    
    # Prepare arguments for the workers
    search_space = product(range(min_x, max_x + 1), range(min_y, max_y + 1))
    worker_args = ((pt, poly_coords) for pt in search_space)

    # Use ProcessPoolExecutor for CPU-bound tasks
    with ProcessPoolExecutor() as executor:
        # chunksize=100-500 prevents the overhead of starting new tasks constantly
        results = list(tqdm(
            executor.map(check_point_worker, worker_args, chunksize=500), 
            total=total_cells, 
            desc="Grid Mapping", 
            bar_format=custom_bar
        ))
        
    # Filter out None values and build the set
    valid_points = {res for res in results if res is not None}

    # --- Part 2 Scanning (Already fast due to early-exit) ---
    combos = list(combinations(poly_coords, 2))
    combos.sort(key=lambda p: get_area(p[0], p[1]), reverse=True)

    max_area_p2 = 0
    for p1, p2 in tqdm(combos, desc="Checking Rects", bar_format=custom_bar):
        area = get_area(p1, p2)
        if area <= max_area_p2:
            break
            
        x_min, x_max = sorted([p1[0], p2[0]])
        y_min, y_max = sorted([p1[1], p2[1]])

        is_valid = True
        for x in range(x_min, x_max + 1):
            if (x, y_min) not in valid_points or (x, y_max) not in valid_points:
                is_valid = False; break
        if not is_valid: continue

        for y in range(y_min + 1, y_max):
            if (x_min, y) not in valid_points or (x_max, y) not in valid_points:
                is_valid = False; break
        
        if is_valid:
            max_area_p2 = area

    print(f"\nPart 2: {max_area_p2}")

if __name__ == "__main__":
    solve()