import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((2, 5, 1, 3, 4, 7), 3),
        ((1, 2, 3, 4, 4, 3, 2, 1), 4),
    }
    cases.add(((1,) * 500 + (1000,) * 500, 500))
    while len(cases) < 600:
        n = rng.randint(1, 500)
        cases.add((tuple(rng.randint(1, 1000) for _ in range(2 * n)), n))
    calls = [f"candidate(nums={list(nums)!r}, n={n})" for nums, n in cases]
    calls.extend(["candidate(nums=[1, 1, 2, 2], n=2)"])
    return list(dict.fromkeys(calls))
