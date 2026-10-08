import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1, 4, 2, 5, 3), (1, 2), (10, 11, 12)}
    cases.add((1,) * 99 + (1000,))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 1000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(arr={list(values)!r})" for values in cases]
