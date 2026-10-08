import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(3, 1), (2, 2, 2), (3, 2, 1, 5), (1,), (1, 1)}
    cases.add((100_000,))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100_000) for _ in range(rng.randint(1, 16))))
    assert all(
        1 <= len(nums) <= 16 and all(1 <= value <= 100_000 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
