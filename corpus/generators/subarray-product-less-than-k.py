import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((10, 5, 2, 6), 100),
        ((1, 2, 3), 0),
        ((1, 1, 1), 1),
        ((1000,) * 30_000, 10**6),
    }
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 1000) for _ in range(rng.randint(1, 100)))
        cases.add((nums, rng.randint(0, 10**6)))
    assert all(
        1 <= len(nums) <= 30_000
        and 0 <= k <= 10**6
        and all(1 <= value <= 1000 for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
