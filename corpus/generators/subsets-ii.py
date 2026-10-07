import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 2, 2), (0,)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(-10, 10) for _ in range(rng.randint(1, 10))))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
