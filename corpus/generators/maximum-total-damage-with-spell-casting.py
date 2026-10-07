import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 1, 3, 4), (7, 1, 6, 6)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(power={list(power)!r})" for power in cases]
