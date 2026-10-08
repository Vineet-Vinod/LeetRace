import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(4, 9, 6, 10), (6, 8, 11, 12), (5, 8, 3)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 1000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
