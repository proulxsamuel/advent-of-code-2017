from collections import defaultdict


def create_graph(connections):
    """Create a graph from the given connections."""
    graph = defaultdict(set)
    for connection in connections:
        source = connection[0]
        for target in connection[1:]:
            graph[source].add(target)
            graph[target].add(source)
    return graph


def is_connected(source, target):
    """Check if source is connected to target in graph."""
    visited = [source]
    to_visit = set(graph[source])
    while len(to_visit) > 0:
        vertex = to_visit.pop()
        visited.append(vertex)
        if vertex == target:
            return True
        else:
            for vertex in graph[vertex]:
                if vertex not in visited:
                    to_visit.add(vertex)
    return False


def find_group(id=0, limited_to=None):
    """Return group of all vertices connected to id."""
    group = [id]
    limited_to = limited_to if limited_to else graph
    for vertex in limited_to:
        if is_connected(vertex, id):
            group.append(vertex)
    return group


def find_groups():
    """Return all groups of vertices that are connected together."""
    groups = []
    available = list(graph.keys())
    for vertex in graph:
        present = False
        for group in groups:
            if vertex in group:
                present = True
                break
        if not present:
            group = find_group(vertex, available)
            groups.append(group)
            for vertex in group:
                if vertex in available:
                    available.remove(vertex)
    return groups


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    input = input.replace(" <-> ", ", ")
    connections = [list(map(int, line.split(", "))) for line in input.splitlines()]
    graph = create_graph(connections)
    print(len(find_group()))
    print(len(find_groups()))
