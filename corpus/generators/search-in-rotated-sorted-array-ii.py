import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((2, 5, 6, 0, 0, 1, 2), 0),
        ((2, 5, 6, 0, 0, 1, 2), 3),
        ((1, 1, 1, 1), 1),
        ((1,), 0),
        ((0,) * 5000, 0),
        ((0,) * 5000, 1),
        ((10_000, -10_000), 10_000),
        ((10_000, -10_000), -10_000),
    }
    while len(cases) < 600:
        base = sorted(rng.randint(-10_000, 10_000) for _ in range(rng.randint(1, 80)))
        pivot = rng.randrange(len(base))
        nums = tuple(base[pivot:] + base[:pivot])
        if rng.random() < 0.5:
            target = rng.choice(nums)
        else:
            target = 10_000 if max(nums) < 10_000 else -10_000
            if target in nums:
                target = -10_000 if min(nums) > -10_000 else 0
        cases.add((nums, target))
    assert all(
        1 <= len(nums) <= 5000
        and all(-10_000 <= value <= 10_000 for value in nums)
        and -10_000 <= target <= 10_000
        for nums, target in cases
    )
    return [
        f"candidate(nums={list(nums)!r}, target={target})"
        for nums, target in sorted(cases)
    ]
