import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(4, 2, 5, 3), (5, 6, 7, 8), (6, 2, 1, 2, 4, 5)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**5) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
