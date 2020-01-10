from math import sqrt
from textwrap import wrap


def split(image):
    """Split image into even squares."""
    size = len(image)
    subsize = 2 if size % 2 == 0 else 3
    length = size // subsize
    quantity = length**2
    squares = ["" for i in range(quantity)]
    for i in range(quantity):
        row = i // length * subsize
        for j in range(row, row + subsize):
            col = i % length * subsize
            for k in range(col, col + subsize):
                squares[i] += image[j][k]
    return [wrap(square, subsize) for square in squares]


def merge(squares):
    """Merge squares back into an image."""
    quantity = len(squares)
    length = int(sqrt(quantity))
    subsize = len(squares[0][0])
    size = subsize * length
    image = ""
    for i in range(size):
        row = i // subsize
        y = i % subsize
        for j in range(size):
            col = j // subsize
            x = j % subsize
            pos = row * length + col
            val = squares[pos][y][x]
            image += val
    return wrap(image, size)


def hflip(matrix):
    """Flip the matrix horizontally."""
    return [row[::-1] for row in matrix]


def vflip(matrix):
    """Flip the matrix vertically."""
    return [row[:] for row in matrix][::-1]


def bflip(matrix):
    """Flip the matrix bi-directionally."""
    return hflip(vflip(matrix))


def rotate(matrix, reps=1):
    """Rotate the matrix 90 degrees clockwise."""
    if reps == 0:
        return matrix
    else:
        rotated = list(''.join(parts) for parts in zip(*reversed(matrix)))
        return rotate(rotated, reps - 1)


def generate(image, reps):
    """Generate an image by enhancing its subparts."""
    for i in range(reps):
        squares = split(image)
        squares = [rules['/'.join(square)].split('/') for square in squares]
        image = merge(squares)
    return image


def output(image):
    """Output the given image."""
    for row in image:
        print(row)
    print()


def count_on_pixels(image):
    """Count the number of 'on' pixels in the image."""
    count = 0
    for row in image:
        count += row.count('#')
    return count


def generate_rules(ruleset):
    """Generate all rules using transformations from ruleset."""
    rules = {}
    for entry in ruleset:
        output = entry[1]
        matrix = entry[0].split('/')
        for f in [matrix, hflip(matrix), vflip(matrix), bflip(matrix)]:
            for r in [f, rotate(f), rotate(f, 2), rotate(f, 3)]:
                rule = '/'.join(r)
                assert rule not in rules or rules[rule] == output
                rules[rule] = output
    return rules


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    ruleset = (line.split(" => ") for line in input.splitlines())
    rules = generate_rules(ruleset)
    image = [".#.", "..#", "###"]
    print(count_on_pixels(generate(image, 5)))
    print(count_on_pixels(generate(image, 18)))
