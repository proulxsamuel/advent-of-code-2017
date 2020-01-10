def count_steps(squares, decreasing=False):
    """Count the amount of steps required to exit the square sequence."""
    pos = 0
    count = 0
    while pos >= 0 and pos < len(squares):
        prev = pos
        pos += squares[pos]
        squares[prev] += -1 if decreasing and squares[prev] >= 3 else 1
        count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    squares = list(map(int, input.splitlines()))
    print(count_steps(squares[:]))
    print(count_steps(squares[:], True))
