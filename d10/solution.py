def reverse(elements, pos, n):
    """Reverse n elements from the list starting at given position."""
    size = len(elements)
    offset = 0
    while offset < n // 2:
        pos1 = (pos + offset) % size
        pos2 = (pos + n - 1 - offset) % size
        elements[pos1], elements[pos2] = elements[pos2], elements[pos1]
        offset += 1


def sparse_hash(elements, lengths, repetitions=1):
    """Return sparse hash of elements produced with given lengths."""
    hash = elements[:]
    pos = 0
    skip = 0
    for i in range(repetitions):
        for length in lengths:
            reverse(hash, pos, length)
            pos += length + skip
            skip += 1
    return hash


def dense_hash(sparse_hash):
    """Return dense hash of given sparse hash."""
    hash = []
    for i in range(len(sparse_hash) // 16):
        total = 0
        for j in range(16):
            total = total ^ sparse_hash[i * 16 + j]
        hash.append(total)
    return hash


def knot_hash(dense_hash):
    """Return knot hash of given dense hash."""
    hash = []
    for number in dense_hash:
        hexvalue = hex(number)[-2:]
        if hexvalue[0] == 'x':
            hexvalue = '0' + hexvalue[1]
        hash.append(hexvalue)
    return hash


def generate_knot_hash(lengths):
    """Generate knot hash from elements with given lengths."""
    elements = [i for i in range(256)]
    hash = sparse_hash(elements, decode_byte_lengths(lengths), 64)
    hash = dense_hash(hash)
    hash = knot_hash(hash)
    return ''.join(hash)


def multiply(elements, n=2):
    """Return product of first n elements."""
    product = 1
    for i in range(n):
        product *= elements[i]
    return product


def decode_byte_lengths(input):
    """Return hash lengths from ascii values of input."""
    lengths = []
    for char in input:
        lengths.append(ord(char))
    return lengths + [17, 31, 73, 47, 23]


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    elements = [i for i in range(256)]
    lengths = [int(value) for value in input.split(',')]
    print(multiply(sparse_hash(elements, lengths), 2))
    print(generate_knot_hash(input))
