import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 1, 1, 2, 2, 3), 2), ((1,), 1)}
    while len(cases) < 600:
        nums = tuple(rng.randint(-10000, 10000) for _ in range(rng.randint(1, 100)))
        k = rng.randint(1, len(set(nums)))
        cases.add((nums, k))
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in cases]
