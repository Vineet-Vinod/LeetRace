import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(3, 6, 5, 1, 8), (4,), (1, 2, 3, 4, 4), (1,), (3,)}
    cases.add(tuple([10_000] * 40_000))
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 10_000) for _ in range(rng.randint(1, 70)))
        cases.add(nums)
    assert all(
        1 <= len(nums) <= 40_000 and all(1 <= value <= 10_000 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
