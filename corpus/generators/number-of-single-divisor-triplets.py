import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(4, 6, 7, 3, 2), (1, 2, 2), (1, 1, 1)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100) for _ in range(rng.randint(3, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
