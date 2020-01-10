from re import fullmatch


def traverse(diagram):
    """Traverse routing diagram. Return path and number of steps."""
    pos = (diagram[0].index('|'), 0)
    dir = (0, 1)
    path = ""
    steps = 0
    done = False
    while not done:
        x, y = pos
        char = diagram[y][x]
        if char == '+':  # If corner, turn in available direction
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dirs.remove(dir)
            dirs.remove(tuple(v * -1 for v in dir))
            for newdir in dirs:
                try:
                    nextx, nexty = tuple(v + dv for v, dv in zip(pos, newdir))
                    next = diagram[nexty][nextx]
                except IndexError:
                    continue
                if fullmatch("[|\-A-Z]", next):
                    dir = newdir
                    break
        elif char.isalpha():  # If checkpoint, add to path
            path += char
        elif char == ' ':  # If path ended
            done = True
        if not done:
            pos = tuple(v + dv for v, dv in zip(pos, dir))
            steps += 1
    return path, steps


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
    diagram = input.splitlines()
    for value in traverse(diagram):
        print(value)
