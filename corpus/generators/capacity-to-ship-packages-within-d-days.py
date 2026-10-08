import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1,), 1),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5),
        ((3, 2, 2, 4, 1, 4), 3),
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        weights = tuple(rng.randint(1, 500) for _ in range(n))
        cases.add((weights, rng.randint(1, n)))
    return [
        f"candidate(weights={list(weights)!r}, days={days})" for weights, days in cases
    ]
