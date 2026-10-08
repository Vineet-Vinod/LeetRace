import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 2, 3, 4), (-1, 4, 5, 6)), ((1, -2, -5, 0, 10), (0, -2, -1, -7, -4))}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        cases.add(
            (
                tuple(rng.randint(-(10**6), 10**6) for _ in range(n)),
                tuple(rng.randint(-(10**6), 10**6) for _ in range(n)),
            )
        )
    return [f"candidate(arr1={list(a)!r}, arr2={list(b)!r})" for a, b in cases]
