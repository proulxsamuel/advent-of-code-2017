import sys
sys.path.append("../")
from d10.solution import generate_knot_hash


def compute_grid(key):
    """Create grid from knot hashes generated with given key."""
    grid = []
    for i in range(128):
        input = key + '-' + str(i)
        hash = generate_knot_hash(input)
        bits = bin(int(hash, 16))[2:].rjust(128, '0')
        grid.append(bits)
    return grid


def count_used_squares():
    """Count the number of used squares in grid."""
    count = 0
    for row in grid:
        count += row.count('1')
    return count


def flood(pos, visited):
    """Visit given position and all non-empty neighbors, recursively."""
    visited.add(pos)
    x, y = pos
    for neighbor in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        dx, dy = neighbor
        newx, newy = x + dx, y + dy
        if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid):
            if grid[newx][newy] == '1' and (newx, newy) not in visited:
                flood((newx, newy), visited)


def count_regions():
    """Count the number of connected regions in grid."""
    count = 0
    visited = set()
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == '1' and (x, y) not in visited:
                flood((x, y), visited)
                count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    grid = compute_grid(input)
    print(count_used_squares())
    print(count_regions())
