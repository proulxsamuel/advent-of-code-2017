def value_following(val, step):
    """Return value in following position of where given value is inserted."""
    buffer = [0]
    pos = 0
    for i in range(1, val + 1):
        pos = (pos + step) % len(buffer) + 1
        buffer.insert(pos, i)
    return buffer[pos + 1] if pos + 1 < len(buffer) else buffer[0]


def value_at_position(position, values, step):
    """Return the value at given position after all values are inserted."""
    current = None
    pos = 0
    for i in range(1, values + 1):
        pos = (pos + step) % i + 1
        if pos == position:
            current = i
    return current


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    step = int(input)
    print(value_following(2017, step))
    print(value_at_position(1, 50000000, step))
