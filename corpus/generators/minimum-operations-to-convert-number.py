import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((2, 4, 12), 2, 12), ((3, 5, 7), 0, -4), ((2, 8, 16), 0, 1)}
    # Add reachable cases by applying one legal operation to an in-range start.
    for _ in range(200):
        nums = tuple(rng.sample(range(-100, 101), rng.randint(1, 8)))
        start = rng.randint(0, 1000)
        value = rng.choice(nums)
        goal = rng.choice((start + value, start - value, start ^ value))
        if goal != start and -(10**9) <= goal <= 10**9:
            cases.add((nums, start, goal))
    while len(cases) < 600:
        nums = tuple(rng.sample(range(-20, 21), rng.randint(1, 8)))
        start = rng.randint(0, 1000)
        goal = rng.choice(
            (rng.randint(-1000, -1), rng.randint(1001, 2000), rng.randint(0, 1000))
        )
        if goal != start:
            cases.add((nums, start, goal))
    calls = [
        f"candidate(nums={list(nums)!r}, start={start}, goal={goal})"
        for nums, start, goal in cases
    ]
    calls.append("candidate(nums=list(range(1000)), start=0, goal=1)")
    for nums, start, goal in cases:
        assert 1 <= len(nums) <= 1000
        assert len(nums) == len(set(nums))
        assert all(-(10**9) <= value <= 10**9 for value in nums)
        assert -(10**9) <= goal <= 10**9
        assert 0 <= start <= 1000 and start != goal
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return sorted(calls)
