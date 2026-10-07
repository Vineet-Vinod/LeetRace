import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(16, 6), (467, 6), (1, 1)}
    while len(cases) < 600:
        n = rng.randint(1, 10**12)
        target = rng.randint(1, 150)
        cases.add((n, target))
    return [f"candidate(n={n}, target={target})" for n, target in cases]
