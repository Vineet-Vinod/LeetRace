import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 1, 4, 2, 3), 5),
        ((5, 6, 7, 8, 9), 4),
        ((3, 2, 20, 1, 1, 3), 10),
        ((1,), 1),
        ((1, 1), 2),
    }
    cases.add((tuple([1] * 100000), 100000))
    cases.add((tuple([10000] * 100000), 10**9))
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 10000) for _ in range(rng.randint(1, 80)))
        if rng.random() < 0.55:
            left = rng.randint(0, len(nums))
            right = rng.randint(0, len(nums) - left)
            if left + right == 0:
                left = 1
            x = (
                sum(nums[:left]) + sum(nums[len(nums) - right :])
                if right
                else sum(nums[:left])
            )
            x = max(1, x)
        else:
            x = rng.randint(sum(nums) + 1, 10**9)
        cases.add((nums, x))
    assert len(cases) == 600 and all(
        1 <= len(a) <= 100000 and 1 <= x <= 10**9 and all(1 <= v <= 10000 for v in a)
        for a, x in cases
    )
    return [f"candidate(nums={list(a)!r}, x={x})" for a, x in sorted(cases)]
