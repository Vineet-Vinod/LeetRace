import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(0, 21), (10, 15)}
    while len(cases) < 600:
        low = rng.randint(0, 2 * 10**9)
        high = rng.randint(low, 2 * 10**9)
        cases.add((low, high))
    return [f"candidate(low={low}, high={high})" for low, high in cases]
