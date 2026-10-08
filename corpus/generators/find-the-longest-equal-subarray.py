import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 3, 2, 3, 1, 3), 3),
        ((1, 1, 2, 2, 1, 1), 2),
        ((1,), 0),
        ((1, 1, 1), 0),
    }
    cases.add(((i % 17 + 1 for i in range(100_000)), 1000))
    cases.add((tuple(i % 2 + 1 for i in range(100_000)), 100_000))
    cases.add((tuple(range(1, 100_001)), 100_000))
    cases = {(tuple(nums), k) for nums, k in cases}
    while len(cases) < 600:
        size = rng.randint(1, 100)
        nums = tuple(rng.randint(1, size) for _ in range(size))
        cases.add((nums, rng.randint(0, len(nums))))
    assert all(
        1 <= len(nums) <= 100_000
        and 0 <= k <= len(nums)
        and all(1 <= value <= len(nums) for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
