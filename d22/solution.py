from collections import defaultdict


def turn_right(dir):
    """Return direction after turning right from current direction."""
    return {
        ( 0, 1): ( 1, 0),
        ( 1, 0): ( 0,-1),
        ( 0,-1): (-1, 0),
        (-1, 0): ( 0, 1),
    }[dir]


def turn_left(dir):
    """Return direction after turning left from current direction."""
    return {
        ( 0, 1): (-1, 0),
        (-1, 0): ( 0,-1),
        ( 0,-1): ( 1, 0),
        ( 1, 0): ( 0, 1),
    }[dir]


def reverse(dir):
    """Return opposite direction from current direction."""
    return tuple(a * -1 for a in dir)


def traverse(grid, bursts, evolved=False):
    """Traverse grid and return number of infecting bursts."""
    grid = grid.copy()
    pos = 0, 0
    dir = 0, 1
    count = 0
    for i in range(bursts):
        node = grid[pos]
        if not evolved:
            if node == '#':
                dir = turn_right(dir)
                grid[pos] = '.'
            else:
                dir = turn_left(dir)
                grid[pos] = '#'
                count += 1
        else:
            if node == '#':
                dir = turn_right(dir)
                grid[pos] = 'F'
            elif node == 'W':
                grid[pos] = '#'
                count += 1
            elif node == 'F':
                dir = reverse(dir)
                grid[pos] = '.'
            else:
                dir = turn_left(dir)
                grid[pos] = 'W'
        pos = tuple(a + b for a, b in zip(pos, dir))
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    x0, y0 = -(input.index('\n') - 1) // 2, -(input.count('\n') - 1) // 2
    grid = defaultdict(lambda: '.')
    for i, row in enumerate(reversed(input.splitlines())):
        for j, val in enumerate(row):
            grid[(y0 + j, x0 + i)] = val
    print(traverse(grid, 10000))
    print(traverse(grid, 10000000, True))
