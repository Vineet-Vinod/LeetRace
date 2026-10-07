import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 2, 3, 3, 2, 2),
        (1, 2, 3, 4),
        (7,) * 100_000,
        (10**6,) * 50,
        (10**6,) * 100_000,
    }
    while len(cases) < 600:
        length = rng.randint(1, 60)
        maximum = rng.randint(1, 10**6)
        run = rng.randint(1, length)
        start = rng.randint(0, length - run)
        nums = [
            rng.randint(1, maximum - 1) if maximum > 1 else 1 for _ in range(length)
        ]
        nums[start : start + run] = [maximum] * run
        cases.add(tuple(nums))
    assert all(
        1 <= len(nums) <= 100_000 and all(1 <= value <= 10**6 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
