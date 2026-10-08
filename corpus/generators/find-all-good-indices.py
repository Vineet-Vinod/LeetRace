import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((2, 1, 1, 1, 3, 4, 1), 2),
        ((2, 1, 1, 2), 2),
        ((4, 3, 2, 1, 1, 2, 3, 4), 2),
        (tuple(range(1, 100_001)), 1),
        ((1_000_000,) * 100_000, 49_999),
    }
    while len(cases) < 600:
        mode = rng.randrange(3)
        if mode == 0:
            k = rng.randint(1, 50)
            left = sorted((rng.randint(1, 1_000_000) for _ in range(k)), reverse=True)
            right = sorted(rng.randint(1, 1_000_000) for _ in range(k))
            nums = tuple(left + [rng.randint(1, 1_000_000)] + right)
        elif mode == 1:
            k = rng.randint(2, 50)
            nums = tuple(range(1, 2 * k + 2))
        else:
            size = rng.randint(3, 100)
            nums = tuple(rng.randint(1, 1_000_000) for _ in range(size))
            k = rng.randint(1, size // 2)
        if mode != 2:
            k = (len(nums) - 1) // 2
        cases.add((nums, k))
    assert all(
        3 <= len(nums) <= 100_000
        and 1 <= k <= len(nums) // 2
        and all(1 <= value <= 1_000_000 for value in nums)
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
