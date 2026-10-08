import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 2), (2, 3), (-1, 1), (-1000, -1000)}
    while len(cases) < 600:
        cases.add((rng.randint(-1000, 1000), rng.randint(-1000, 1000)))
    return [f"candidate(a={a}, b={b})" for a, b in cases]
