import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 0, 2, 1, 3),
        (1, 2),
        (0,),
        (0, 0, 0),
        (10**9,) * 1000,
        (10**9,) * 100_000,
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 10**9) for _ in range(rng.randint(1, 100))))
    assert all(
        1 <= len(nums) <= 100_000 and all(0 <= value <= 10**9 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
