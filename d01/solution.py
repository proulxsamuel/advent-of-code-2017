def sum_match_next(input):
    """Return the sum of all digits that match the following digit."""
    length = len(input)
    sum = 0
    for i in range(length):
        if input[i] == input[(i + 1) % length]:
            sum += int(input[i])
    return sum


def sum_match_halfway(input):
    """Return the sum of all digits that match the digit halfway around."""
    length = len(input)
    sum = 0
    for i in range(length):
        if input[i] == input[(i + length // 2) % length]:
            sum += int(input[i])
    return sum


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    print(sum_match_next(input))
    print(sum_match_halfway(input))
