import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 3, 7, 9, 3), (5, 3, 3), (1,)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**6) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
