import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 1, 1, 1, 1), 3),
        ((1,), 1),
        ((0,) * 20, 0),
        ((0,) * 20, 1),
        ((1000,) + (0,) * 19, 1000),
        ((1000,) + (0,) * 19, -1000),
        ((1,) * 20, 0),
        ((1,) * 20, 20),
        ((1,) * 20, -20),
    }
    while len(cases) < 600:
        size = rng.randint(1, 20)
        values: list[int] = []
        remaining = 1000
        for _ in range(size):
            value = rng.randint(0, remaining)
            values.append(value)
            remaining -= value
        nums = tuple(values)
        if rng.random() < 0.7:
            target = sum(value if rng.random() < 0.5 else -value for value in nums)
        else:
            target = rng.randint(-1000, 1000)
        cases.add((nums, target))
    assert all(
        1 <= len(nums) <= 20
        and all(0 <= value <= 1000 for value in nums)
        and sum(nums) <= 1000
        and -1000 <= target <= 1000
        for nums, target in cases
    )
    return [
        f"candidate(nums={list(nums)!r}, target={target})"
        for nums, target in sorted(cases)
    ]
