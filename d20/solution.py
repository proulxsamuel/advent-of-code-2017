from re import findall
from copy import deepcopy


def order(particles):
    """Return particles in order they tend toward after many iterations."""
    return list(sorted(
        particles,
        key=lambda p: list(reversed([sum(map(abs, v)) for v in p]))))


def closest(particles):
    """Return particle which tends to stay closest to (0, 0, 0)."""
    return particles.index(order(particles)[0])


def update(particles):
    """Move all particles."""
    for p in particles:
        p[1] = [vel + acc for vel, acc in zip(p[1], p[2])]
        p[0] = [pos + vel for pos, vel in zip(p[0], p[1])]


def remaining(particles, reps=50):
    """Return how many particles remain after colliding ones are deleted."""
    particles = deepcopy(particles)
    for i in range(reps):
        to_remove = set()
        for i, p1 in enumerate(particles):
            for j, p2 in enumerate(particles):
                if i != j and p1[0] == p2[0]:
                    to_remove.add(i)
                    to_remove.add(j)
        for index in sorted(to_remove, reverse=True):
            del particles[index]
        update(particles)
    return len(particles)


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read().strip()
    particles = [[[int(val) for val in vector.split(',')]
                  for vector in findall("-?\d+,-?\d+,-?\d+", line)]
                 for line in input.splitlines()]
    print(closest(particles))
    print(remaining(particles))
