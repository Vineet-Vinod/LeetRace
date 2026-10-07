import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 2, 3, 4), 1), ((1, 3, 5, 7), 1), ((1, 5, 7, 8, 5, 3, 4, 2, 1), -2)}
    while len(cases) < 600:
        arr = tuple(rng.randint(-10000, 10000) for _ in range(rng.randint(1, 100)))
        cases.add((arr, rng.randint(-10000, 10000)))
    return [f"candidate(arr={list(arr)!r}, difference={d})" for arr, d in cases]
