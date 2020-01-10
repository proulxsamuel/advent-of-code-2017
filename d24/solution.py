def available(components, port):
    """Return indexes of available components matching given port."""
    return [i for i, component in enumerate(components)
            if component[0] == port or component[1] == port]


def build_all(components, bridge=None, port=0):
    """Return all bridges that can be build from given components."""
    bridges = []
    bridge = bridge if bridge else []
    for index in available(components, port):
        comps = components.copy()
        newbridge = bridge.copy()
        newpart = comps.pop(index)
        newbridge.append(newpart)
        newport = newpart[0] if newpart[0] != port else newpart[1]
        bridges.extend(build_all(comps, newbridge, newport))
    if bridge != []:
        bridges.append(bridge)
    return bridges


def build_strongest(bridges):
    """Return strength of the strongest bridge."""
    return max(sum(sum(part) for part in bridge) for bridge in bridges)


def build_longest(bridges):
    """Return strength of the strongest longest bridge."""
    length = max(len(bridge) for bridge in bridges)
    longests = [bridge for bridge in bridges if len(bridge) == length]
    return build_strongest(longests)


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    components = [tuple(map(int, line.split('/')))
                  for line in input.splitlines()]
    bridges = build_all(components)
    print(build_strongest(bridges))
    print(build_longest(bridges))
