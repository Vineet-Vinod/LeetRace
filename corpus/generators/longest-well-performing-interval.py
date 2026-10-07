import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(9, 9, 6, 0, 6, 6, 9), (6, 6, 6)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 16) for _ in range(rng.randint(1, 100))))
    return [f"candidate(hours={list(hours)!r})" for hours in cases]
