import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((5, 2, 2, 4, 0, 6), 4),
        ((2,), 1),
        ((7,), 0),
        ((7,), 2),
        ((1, 2), 10**9),
        ((1, 9, 3, 8), 1),
    }
    cases.add((tuple([10**9] * 100_000), 0))
    while len(cases) < 600:
        nums = tuple(rng.randint(0, 10**9) for _ in range(rng.randint(1, 80)))
        cases.add((nums, rng.randint(0, 10**9)))
    assert all(
        1 <= len(nums) <= 100_000
        and 0 <= k <= 10**9
        and all(0 <= value <= 10**9 for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
