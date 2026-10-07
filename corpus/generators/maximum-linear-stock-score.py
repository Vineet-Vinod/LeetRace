import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 5, 3, 7, 8), (5, 6, 7, 8, 9)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(prices={list(prices)!r})" for prices in cases]
