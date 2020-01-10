def find_matches(quantity, a, b, afactor, bfactor, amod=None, bmod=None):
    """Find the number of matches in the given number of comparisons."""
    diviser = 2147483647
    bits = 16
    count = 0
    for i in range(quantity):
        a = a * afactor % diviser
        abin = bin(a)[-bits:]
        while amod and not amod(abin):
            a = a * afactor % diviser
            abin = bin(a)[-bits:]
        b = b * bfactor % diviser
        bbin = bin(b)[-bits:]
        while bmod and not bmod(bbin):
            b = b * bfactor % diviser
            bbin = bin(b)[-bits:]
        if abin == bbin:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    a, b = tuple(int(v) for v in input.split() if v.isdigit())
    afactor, bfactor = 16807, 48271
    print(find_matches(40000000, a, b, afactor, bfactor))
    print(find_matches(5000000, a, b, afactor, bfactor,
                       lambda x: x[-2:] == "00",
                       lambda x: x[-3:] == "000"))
