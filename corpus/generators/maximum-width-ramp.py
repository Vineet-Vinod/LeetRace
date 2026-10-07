import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(6, 0, 8, 2, 1, 5), (9, 8, 1, 0, 1, 9, 4, 0, 4, 1)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 50000) for _ in range(rng.randint(2, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
