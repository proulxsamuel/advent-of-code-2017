def largest(banks):
    """Return the index of the largest bank."""
    max = 0
    for i in range(len(banks)):
        if banks[i] > banks[max]:
            max = i
    return max


def distribute(banks):
    """Distribute the blocks of the largest bank over all banks."""
    n = largest(banks)
    blocks = banks[n]
    banks[n] = 0
    while blocks > 0:
        n += 1
        banks[n % len(banks)] += 1
        blocks -= 1
    return banks


def cycle(banks, results=False):
    """Cycle and ditribute the banks until returning to known configuration."""
    cycles = [banks[:]]
    count = 0
    while True:
        count += 1
        banks = distribute(banks)
        if banks in cycles:
            break
        else:
            cycles.append(banks[:])
    if not results:
        return count
    else:
        return count, banks


def size(banks):
    """Return the size of the loop which returns to starting configuration."""
    count, banks = cycle(banks, True)
    count = cycle(banks)
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    banks = list(map(int, input.split("\t")))
    print(cycle(banks))
    print(size(banks))
