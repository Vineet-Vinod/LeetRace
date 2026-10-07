import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(3, 1), (4, 11)}
    while len(cases) < 600:
        n = rng.randint(1, 20)
        cases.add((n, rng.randint(1, (1 << n) - 1)))
    return [f"candidate(n={n}, k={k})" for n, k in cases]
