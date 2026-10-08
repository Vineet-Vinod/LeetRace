import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(4, 3, 2, 6), (100,), (1, -1), (0, 0, 0)}
    cases.add(tuple([100] * 50_000 + [-100] * 50_000))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(-100, 100) for _ in range(rng.randint(1, 100))))
    assert all(
        1 <= len(nums) <= 100_000 and all(-100 <= value <= 100 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
