from re import sub
from collections import Counter


class Program:
    """Program object which might contain sub-programs."""

    def __init__(self, name, weight, subprograms):
        """Create a program of given name, weight and sub-programs names."""
        self.name = name
        self.weight = weight
        self.subprograms = subprograms

    def __repr__(self):
        """Representation of program for outputing."""
        return self.name

    def has_subprograms(self):
        """Check if program has sub-program."""
        return len(self.subprograms) > 0

    def total_weight(self):
        """Find the total weight of this program and its sub-programs."""
        sum = self.weight
        for subprogram in self.subprograms:
            sum += programs[subprogram].total_weight()
        return sum

    def subprograms_weights(self):
        """Return the weights of this program's sub-programs."""
        return [programs[subprogram].total_weight()
                for subprogram in self.subprograms]

    def expected_subprogram_weight(self):
        """Return the expected weight of all subprograms."""
        return Counter(self.subprograms_weights()).most_common(1)[0][0]

    def find_imbalance(self):
        """Return imbalanced subprogram of program, if any."""
        expected = self.expected_subprogram_weight()
        weights = self.subprograms_weights()
        for index, weight in enumerate(weights):
            if weight != expected:
                return programs[self.subprograms[index]]
        return None


def find_root():
    """Find the root program at the bottom of the tower."""
    for name, program in programs.items():
        valid = True
        if program.has_subprograms():
            for othername, otherprogram in programs.items():
                if name in otherprogram.subprograms:
                    valid = False
                    break
        else:
            valid = False
        if valid:
            return program


def find_imbalance(program=None):
    """Find which program is imbalanced and the weight it should be instead."""
    program = program if program else find_root()
    imbalanced = program.find_imbalance()
    if imbalanced.has_subprograms() and imbalanced.find_imbalance():
        return find_imbalance(imbalanced)
    else:
        expected = program.expected_subprogram_weight()
        delta = expected - imbalanced.total_weight()
        return imbalanced, imbalanced.weight + delta


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    input = sub("[(),]|(-> )", "", input)
    programs = {}
    for entry in [line.split(" ") for line in input.splitlines()]:
        programs[entry[0]] = Program(entry[0], int(entry[1]), entry[2:])
    print(find_root())
    print(find_imbalance()[1])
