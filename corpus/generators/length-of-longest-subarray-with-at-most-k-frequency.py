import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 2, 1, 2, 1, 2, 1, 2), 1),
        ((5, 5, 5, 5, 5, 5, 5), 4),
        ((1,), 1),
        ((1, 1, 1), 1),
    }
    cases.add((tuple([10**9] * 100_000), 100_000))
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 90)))
        cases.add((nums, rng.randint(1, len(nums))))
    assert all(
        1 <= len(nums) <= 100_000
        and 1 <= k <= len(nums)
        and all(1 <= value <= 10**9 for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
