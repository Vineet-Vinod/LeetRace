import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, int, int]] = {(1, 4, 2), (5, 4, 4), (5, 0, 0), (0, 0, 0)}
    cases.add((100, 0, 0))
    cases.add((100, 100, 100))
    while len(cases) < 600:
        cases.add((rng.randint(0, 100), rng.randint(0, 100), rng.randint(0, 100)))
    return [f"candidate(amount={list(amount)!r})" for amount in cases]
