import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 2, 3), 2), ((1, 1, 1, 1), 2), ((2, 3, 4, 5), 1)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add((tuple(rng.randint(1, 10**8) for _ in range(n)), rng.randint(1, n)))
    return [f"candidate(happiness={list(values)!r}, k={k})" for values, k in cases]
