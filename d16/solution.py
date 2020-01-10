def dance(programs, moves, reps=1):
    """Return programs after performing moves the given number of times."""
    configs = [programs]
    programs = list(programs)
    for i in range(reps):
        for move in moves:
            op = move[0]
            args = tuple(int(val) if val.isdigit() else val
                         for val in move[1:].split('/'))
            if op == 's':
                n = args[0]
                programs = programs[-n:] + programs[:-n]
            elif op == 'x':
                p1, p2 = args
                programs[p1], programs[p2] = programs[p2], programs[p1]
            elif op == 'p':
                p1, p2 = tuple(programs.index(val) for val in args)
                programs[p1], programs[p2] = programs[p2], programs[p1]
            else:
                raise Exception(f"Unknown move '{move}'")
        config = ''.join(programs)
        if config not in configs:
            configs.append(config)
        else:
            return configs[reps % len(configs)]
    return config


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    moves = input.split(',')
    programs = 'abcdefghijklmnop'
    print(dance(programs, moves))
    print(dance(programs, moves, 1000000000))
