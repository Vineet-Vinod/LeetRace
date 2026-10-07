import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (8, 6, 1, 5, 3),
        (5, 4, 8, 7, 10, 2),
        (6, 5, 4, 3, 4, 5),
        (1, 2, 1),
    }
    mountain = [10**8] * 100_000
    mountain[:3] = [3, 1, 2]
    cases.add(tuple(mountain))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**8) for _ in range(rng.randint(3, 90))))
    assert all(
        3 <= len(nums) <= 100_000 and all(1 <= value <= 10**8 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
