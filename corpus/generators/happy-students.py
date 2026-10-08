import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1, 1), (6, 0, 3, 3, 6, 7, 2, 7), (0,), (0, 1, 2)}
    cases.add(tuple([0] * 100_000))
    while len(cases) < 600:
        size = rng.randint(1, 80)
        cases.add(tuple(rng.randint(0, size - 1) for _ in range(size)))
    assert all(
        1 <= len(nums) <= 100_000 and all(0 <= value < len(nums) for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
