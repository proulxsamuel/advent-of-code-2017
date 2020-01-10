def move(pos, direction):
    """Return position after moving in given direction."""
    x, y, z = pos
    dx, dy, dz = {
        'n':  ( 0, 1,-1),
        's':  ( 0,-1, 1),
        'se': ( 1,-1, 0),
        'nw': (-1, 1, 0),
        'ne': ( 1, 0,-1),
        'sw': (-1, 0, 1),
    }[direction]
    return (x + dx, y + dy, z + dz)


def distance_after(steps, overall_max=False):
    """Return the distance from origin after steps taken."""
    distance = 0
    pos = (0, 0, 0)
    for step in steps:
        pos = move(pos, step)
        if overall_max:
            distance = max(distance, max(map(abs, pos)))
    if not overall_max:
        distance = max(map(abs, pos))
    return distance


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    steps = input.split(',')
    print(distance_after(steps))
    print(distance_after(steps, True))
