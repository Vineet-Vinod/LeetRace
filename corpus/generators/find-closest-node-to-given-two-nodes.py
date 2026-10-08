import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 2, 3, -1), 0, 1), ((1, 2, -1), 0, 2)}
    while len(cases) < 600:
        n = rng.randint(2, 80)
        edges = tuple(
            rng.choice([-1] + [v for v in range(n) if v != node]) for node in range(n)
        )
        cases.add((edges, rng.randrange(n), rng.randrange(n)))
    return [
        f"candidate(edges={list(edges)!r}, node1={a}, node2={b})"
        for edges, a, b in cases
    ]
