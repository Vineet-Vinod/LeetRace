import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((3, 6, 7, 11), 8), ((30, 11, 23, 4, 20), 5), ((30, 11, 23, 4, 20), 6)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        piles = tuple(rng.randint(1, 10**9) for _ in range(n))
        cases.add((piles, rng.randint(n, 10**9)))
    return [f"candidate(piles={list(piles)!r}, h={h})" for piles, h in cases]
