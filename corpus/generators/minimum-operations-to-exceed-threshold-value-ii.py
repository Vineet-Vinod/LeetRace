import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 11, 10, 1, 3), 10), ((1, 1, 2, 4, 9), 20)}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        nums = tuple(rng.randint(1, 1000) for _ in range(n))
        cases.add((nums, rng.randint(1, min(10**9, sum(nums)))))
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in cases]
