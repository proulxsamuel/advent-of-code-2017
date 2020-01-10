from collections import defaultdict


def find_largest(overall=False):
    """Find the largest register value after all instructions or overall."""
    largest = 0
    registers = defaultdict(int)
    for instruction in instructions:
        exec(instruction)
        if overall:
            largest = max(largest, max(registers.values()))
    if not overall:
        largest = max(largest, max(registers.values()))
    return largest


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    instructions = []
    for line in input.splitlines():
        line = line.replace("inc", "+=").replace("dec", "-=")
        parts = line.split(" ")
        parts[0] = f"registers['{parts[0]}']"
        parts[4] = f"registers['{parts[4]}']"
        instruction = " ".join(parts[3:7]) + ": " + " ".join(parts[0:3])
        instructions.append(instruction)
    print(find_largest())
    print(find_largest(overall=True))
