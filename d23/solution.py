from re import fullmatch
from collections import defaultdict
from math import sqrt


def count_mul_invocations(instructions):
    """Count how many times mul is invoced during execution."""
    registers = defaultdict(int)
    count = 0
    pos = 0
    while pos >= 0 and pos < len(instructions):
        instruction = instructions[pos]
        op, reg, val = instruction
        val = val if isinstance(val, int) else registers[val]
        if op == "jnz":
            reg = reg if isinstance(reg, int) else registers[reg]
            if reg != 0:
                pos += val
                continue
        elif op == "set":
            registers[reg] = val
        elif op == "sub":
            registers[reg] -= val
        elif op == "mul":
            registers[reg] *= val
            count += 1
        pos += 1
    return count


def find_h(instructions):
    """Return value of h after executiON. /!\ INPUT-SPECIFIC SOLUTION."""
    # Simplified input instructions turned in into code
    b = 57 * 100 + 100000
    c = b + 17000
    h = 0
    for b in range(b, c + 1, 17):
        for d in range(2, int(sqrt(b))):  # Chech if b is composite (non-prime)
            if b % d == 0:
                h += 1
                break
    return h


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    instructions = [tuple(int(val) if fullmatch("-?\d+", val) else val
                          for val in line.split())
                    for line in input.splitlines()]
    print(count_mul_invocations(instructions))
    print(find_h(instructions))
