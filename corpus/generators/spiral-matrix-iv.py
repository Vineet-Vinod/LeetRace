import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(3, 5, (3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0)), (1, 4, (0, 1, 2))}
    while len(cases) < 600:
        m, n = rng.randint(1, 20), rng.randint(1, 20)
        length = rng.randint(1, m * n)
        values = tuple(rng.randint(0, 1000) for _ in range(length))
        cases.add((m, n, values))
    return [
        f"candidate(m={m}, n={n}, head=list_node({list(values)!r}))"
        for m, n, values in cases
    ]
