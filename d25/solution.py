from collections import defaultdict
from re import search, findall


def diagnostic_checksum(state, steps, rules):
    """Perform the diagnostic checksum after executing Turing machine."""
    tape = defaultdict(int)
    pos = 0
    for i in range(steps):
        value = tape[pos]
        tape[pos], offset, state = rules[state][value]
        pos += offset
    return sum(tape.values())


def read_rules(input):
    """Return initial state, number of steps and ruleset stated in input."""
    initial_state = search("(?<=Begin in state )[A-Z]", input).group()
    steps = int(search("\d+(?= steps)", input).group())
    states = findall("(?<=In state )[A-Z]", input)
    values = list(map(int, findall("(?<=value is )\d", input)))
    new_values = list(map(int, findall("(?<=value )\d", input)))
    new_pos = [1 if val == "right" else -1
               for val in findall("left|right", input)]
    new_states = findall("(?<=with state )[A-Z]", input)
    rules = {state: {values[j]: (new_values[j], new_pos[j], new_states[j])
                     for j in range(2 * i, 2 * i + 2)}
             for i, state in enumerate(states)}
    return initial_state, steps, rules


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    print(diagnostic_checksum(*read_rules(input)))
