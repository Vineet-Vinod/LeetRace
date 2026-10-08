import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((3, 1, 4, 1, 5), 2),
        ((1, 2, 3, 4, 5), 1),
        ((1, 3, 1, 5, 4), 0),
        ((-(10**7), 0, 10**7), 10**7),
        ((4,) * 10_000, 0),
        ((10**7,) * 10_000, 10**7),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        if rng.random() < 0.7:
            gap = rng.randint(0, 1000)
            base = rng.randint(-(10**7), 10**7 - (size - 1) * gap)
            if gap == 0:
                nums = (base,) * size
            else:
                nums = tuple(base + index * gap for index in range(size))
            cases.add((nums, gap))
        else:
            nums = tuple(rng.randint(-(10**7), 10**7) for _ in range(size))
            cases.add((nums, rng.randint(0, 10**7)))
    assert all(
        1 <= len(nums) <= 10_000
        and all(-(10**7) <= value <= 10**7 for value in nums)
        and 0 <= k <= 10**7
        for nums, k in cases
    )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in sorted(cases)]
