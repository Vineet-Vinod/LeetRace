import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 1, 3, 5, 4, 6, 7), 2), ((3, 2, 1), 10)}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        arr = tuple(rng.sample(range(1, 10**6 + 1), n))
        cases.add((arr, rng.randint(1, 10**9)))
    return [f"candidate(arr={list(arr)!r}, k={k})" for arr, k in cases]
