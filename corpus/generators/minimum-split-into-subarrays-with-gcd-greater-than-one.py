import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(12, 6, 3, 14, 8), (4, 12, 6, 14)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(2, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
