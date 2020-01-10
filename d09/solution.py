from re import sub, findall


def compute_score(input):
    """Compute the score of the character group."""
    input = sub("<[^>]*>", "", input)
    total_score = 0
    current_score = 0
    for char in input:
        if char == '{':
            current_score += 1
            total_score += current_score
        elif char == '}':
            current_score -= 1
    return total_score


def count_garbage(input):
    """Count the length of garbage in the input."""
    garbage = findall("<[^>]*>", input)
    count = 0
    for group in garbage:
        group = group[1:-1]
        count += len(group)
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
    input = sub("!.", "", input)
    print(compute_score(input))
    print(count_garbage(input))
