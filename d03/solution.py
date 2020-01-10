def turn(direction):
    """Return new direction after turning left 90 degrees."""
    return {
        ( 1, 0): ( 0, 1),
        ( 0, 1): (-1, 0),
        (-1, 0): ( 0,-1),
        ( 0,-1): ( 1, 0),
    }[direction]


def move(pos, direction):
    """Return position after moving one step in given direction."""
    return (pos[0] + direction[0], pos[1] + direction[1])


def locate(number):
    """Return position of the given number in the incremental spiral."""
    pos = (0, 0)
    direction = (1, 0)
    length = 0
    max = 1
    prev = 0
    i = 1
    while i != number:
        i += 1
        pos = move(pos, direction)
        length += 1
        if length == max:
            direction = turn(direction)
            length = 0
            if max != prev:
                prev = max
            else:
                prev = max
                max += 1
    return pos


def distance(number):
    """Return the distance between the number's position and the origin."""
    pos = locate(number)
    return abs(pos[0]) + abs(pos[1])


def sum_of_neighbors(pos, positions):
    """Return the sum of the existing neighbors from given position."""
    neighbor_offsets = [
        ( 1, 0),
        ( 1, 1),
        ( 0, 1),
        (-1, 1),
        (-1, 0),
        (-1,-1),
        ( 0,-1),
        ( 1,-1),
    ]
    sum = 0
    for offset in neighbor_offsets:
        neighbor_position = (pos[0] + offset[0], pos[1] + offset[1])
        if neighbor_position in positions:
            sum += positions[neighbor_position]
    return sum


def first_after(number):
    """Return the first value in neighbor sum spiral larger than number."""
    positions = {(0, 0): 1}
    pos = (0, 0)
    direction = (1, 0)
    length = 0
    max = 1
    prev = 0
    i = 1
    value = 1
    while value < number:
        i += 1
        pos = move(pos, direction)
        length += 1
        if length == max:
            direction = turn(direction)
            length = 0
            if max != prev:
                prev = max
            else:
                prev = max
                max += 1
        value = sum_of_neighbors(pos, positions)
        positions[pos] = value
    return value


if __name__ == "__main__":
    with open("input.txt") as file:
        input = int(file.read())
    print(distance(input))
    print(first_after(input))
