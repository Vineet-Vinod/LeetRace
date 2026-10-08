import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(3, 1, 3, 2, 4, 3), (1, 2, 2, 2, 2), (5,)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
