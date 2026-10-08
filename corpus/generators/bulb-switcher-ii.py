import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(n, p) for n in range(1, 31) for p in range(0, 20)}
    while len(cases) < 600:
        cases.add((rng.randint(1, 1000), rng.randint(0, 1000)))
    return [f"candidate(n={n}, presses={p})" for n, p in cases]
