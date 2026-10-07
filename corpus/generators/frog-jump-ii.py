import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(0, 2, 5, 6, 7), (0, 3, 9)}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        stones = [0]
        for _ in range(n - 1):
            stones.append(stones[-1] + rng.randint(1, 10**6))
        cases.add(tuple(stones))
    return [f"candidate(stones={list(stones)!r})" for stones in cases]
