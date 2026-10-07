import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 2, 1, 2, 1), (100, 1, 1000), (1, 2, 3, 4, 5)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(arr={list(arr)!r})" for arr in cases]
