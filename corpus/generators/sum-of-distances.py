import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 3, 1, 1, 2), (0, 5, 3)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
