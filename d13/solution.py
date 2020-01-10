def compute_trip_severity():
    """Compute the severity of the traversal of the layers."""
    severity = 0
    for depth, range in layers.items():
        if depth % (2 * range - 2) == 0:
            severity += depth * range
    return severity


def compute_safe_delay():
    """Compute the shortest delay to safely traverse layers."""
    delay = 0
    safe = False
    while not safe:
        safe = True
        for depth, range in layers.items():
            if (depth + delay) % (2 * range - 2) == 0:
                safe = False
                break
        if not safe:
            delay += 1
    return delay


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    layers = {}
    for line in input.splitlines():
        depth, range = tuple(int(value) for value in line.split(": "))
        layers[depth] = range
    print(compute_trip_severity())
    print(compute_safe_delay())
