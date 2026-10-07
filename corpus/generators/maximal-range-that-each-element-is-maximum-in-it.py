import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (3, 4, 1, 6, 2),
        (1, 5, 4, 3, 6),
        (1, 2, 3, 4, 5),
        (1,),
        (100_000, 99_999, 99_998),
    }
    cases.add(tuple(range(1, 100_001)))
    while len(cases) < 600:
        size = rng.randint(1, 100)
        cases.add(tuple(rng.sample(range(1, 100_001), size)))
    assert all(
        1 <= len(nums) <= 100_000
        and len(set(nums)) == len(nums)
        and all(1 <= value <= 100_000 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
