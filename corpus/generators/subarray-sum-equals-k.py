import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 1, 1), 2), ((1, 2, 3), 3), ((0,) * 20000, 0), ((1,) * 20000, 100)}
    while len(cases) < 300:
        n = rng.randint(1, 80)
        nums = tuple(rng.randint(-20, 20) for _ in range(n))
        left = rng.randrange(n)
        right = rng.randrange(left + 1, n + 1)
        target = sum(nums[left:right])
        cases.add((nums, target))
    while len(cases) < 600:
        n = rng.randint(1, 80)
        nums = tuple(rng.randint(-20, 20) for _ in range(n))
        target = rng.choice((-(10**7), 10**7))
        cases.add((nums, target))
    calls = [f"candidate(nums={list(nums)!r}, k={target})" for nums, target in cases]
    assert len(calls) == len(set(calls)) and 500 <= len(calls) <= 999
    assert all(
        1 <= len(nums) <= 20000
        and all(-1000 <= x <= 1000 for x in nums)
        and -(10**7) <= k <= 10**7
        for nums, k in cases
    )
    return calls
