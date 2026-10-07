import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((9, 3, 1, 2, 6, 3), 3),
        ((4,), 7),
        ((10**9,), 10**9),
        ((6,) * 1000, 6),
        ((12, 6, 18, 24, 6), 6),
    }
    while len(cases) < 600:
        k = rng.randint(1, 100)
        size = rng.randint(1, 100)
        if rng.random() < 0.65:
            nums = tuple(k * rng.randint(1, max(1, 10**9 // k)) for _ in range(size))
        else:
            nums = tuple(rng.randint(1, 1000) for _ in range(size))
        cases.add((nums, k))
    assert all(
        1 <= len(nums) <= 1000
        and 1 <= k <= 10**9
        and all(1 <= value <= 10**9 for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
