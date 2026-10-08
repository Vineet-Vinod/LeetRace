import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (3, -1, -5, 2, 5, -9),
        (-4, -5, -4),
        (0,),
        (-9, 9),
        (1,),
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(-9, 9) for _ in range(rng.randint(1, 13))))
    assert all(
        1 <= len(nums) <= 13 and all(-9 <= value <= 9 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
