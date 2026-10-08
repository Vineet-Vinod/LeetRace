import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((), 0),
        ((5, 7, 7, 8, 8, 10), 8),
        ((5, 7, 7, 8, 8, 10), 6),
        ((1,), 1),
    }
    cases.add((tuple([1] * 100_000), 10**9))
    while len(cases) < 600:
        nums = tuple(sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 80))))
        target = rng.randint(-105, 105)
        cases.add((nums, target))
    assert all(
        len(nums) <= 100_000
        and tuple(sorted(nums)) == nums
        and all(-(10**9) <= value <= 10**9 for value in nums)
        and -(10**9) <= target <= 10**9
        for nums, target in cases
    )
    return [
        f"candidate(nums={list(nums)!r}, target={target})"
        for nums, target in sorted(cases)
    ]
