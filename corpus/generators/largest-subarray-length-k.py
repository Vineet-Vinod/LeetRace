import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 4, 5, 2, 3), 3),
        ((1, 4, 5, 2, 3), 1),
        (tuple(range(1, 100_001)), 50_000),
    }
    cases.add(((1, 1_000_000_000), 1))
    cases.add((tuple(range(1, 100_000)) + (1_000_000_000,), 1))
    while len(cases) < 600:
        size = rng.randint(1, 300)
        nums = tuple(rng.sample(range(1, 1_000_000_001), size))
        cases.add((nums, rng.randint(1, size)))
    calls = [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in cases]
    calls.extend(["candidate(nums=[1, 4, 5, 2, 3], k=4)"])
    return list(dict.fromkeys(calls))
