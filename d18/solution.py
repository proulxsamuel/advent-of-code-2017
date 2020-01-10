from collections import defaultdict
from re import fullmatch


def recover(instructions):
    """Return frequency at first recover operation."""
    regs = defaultdict(int)
    frequency = None
    pos = 0
    while pos >= 0 and pos < len(instructions):

        # Fetch and decode instruction
        instruction = instructions[pos]
        if len(instruction) == 2:
            op, reg = tuple(instruction)
        elif len(instruction) == 3:
            op, reg, arg = tuple(instruction)
            val = int(arg) if fullmatch("-?\d+", arg) else regs[arg]
        else:
            raise Exception("Too many arguments.")

        # Execute instruction
        if op == "snd":
            val = int(reg) if fullmatch("-?\d+", reg) else regs[reg]
            frequency = val
        elif op == "rcv":
            val = int(reg) if fullmatch("-?\d+", reg) else regs[reg]
            if val != 0:
                return frequency
        elif op == "jgz":
            reg = int(reg) if fullmatch("-?\d+", reg) else regs[reg]
            if reg > 0:
                pos += val
                continue
        elif op == "set":
            regs[reg] = val
        elif op == "add":
            regs[reg] += val
        elif op == "mul":
            regs[reg] *= val
        elif op == "mod":
            regs[reg] %= val
        else:
            raise Exception(f"Unrecognized operation '{op}'")
        pos += 1


class Program:
    """Program which executes a series of instruction in parallel."""

    id = -1

    def __init__(self, instructions):
        """Create a program which executes given instructions."""
        self.instructions = instructions
        self.regs = defaultdict(int)
        Program.id += 1
        self.id = Program.id
        self.regs['p'] = self.id
        self.pos = 0
        self.sent = 0

    def run(self, input=None):
        """Run the program until it requires input. Return output produced."""
        output = []
        while self.pos >= 0 and self.pos < len(self.instructions):

            # Fetch and decode instruction
            instruction = self.instructions[self.pos]
            if len(instruction) == 2:
                op, reg = tuple(instruction)
            elif len(instruction) == 3:
                op, reg, arg = tuple(instruction)
                val = int(arg) if fullmatch("-?\d+", arg) else self.regs[arg]
            else:
                raise Exception("Too many arguments.")

            # Execute instruction
            if op == "snd":
                val = int(reg) if fullmatch("-?\d+", reg) else self.regs[reg]
                output.append(val)
            elif op == "rcv":
                if input and len(input) > 0:
                    self.regs[reg] = input.pop(0)
                else:
                    break
            elif op == "jgz":
                reg = int(reg) if fullmatch("-?\d+", reg) else self.regs[reg]
                if reg > 0:
                    self.pos += val
                    continue
            elif op == "set":
                self.regs[reg] = val
            elif op == "add":
                self.regs[reg] += val
            elif op == "mul":
                self.regs[reg] *= val
            elif op == "mod":
                self.regs[reg] %= val
            else:
                raise Exception(f"Unrecognized operation '{op}'")
            self.pos += 1
        self.sent += len(output)
        return output


def run(instructions):
    """Run instructions on two programs in parallel."""
    p0 = Program(instructions)
    p1 = Program(instructions)
    o0, o1 = p0.run(), p1.run()
    while len(o0) > 0 or len(o1) > 0:
        o0, o1 = p0.run(o1), p1.run(o0)
    return p1.sent


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    instructions = [line.split() for line in input.splitlines()]
    print(recover(instructions))
    print(run(instructions))
