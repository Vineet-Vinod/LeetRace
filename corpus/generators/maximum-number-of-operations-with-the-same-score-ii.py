import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (3, 2, 1, 2, 3, 4),
        (3, 2, 6, 1, 4),
        (5, 5),
        (7,) * 2000,
        (1, 1000) * 1000,
    }
    while len(cases) < 600:
        size = rng.randint(2, 100)
        mode = rng.randrange(3)
        if mode == 0:
            value = rng.randint(1, 1000)
            nums = (value,) * size
        elif mode == 1:
            first, second = rng.randint(1, 1000), rng.randint(1, 1000)
            nums = tuple(first if index % 2 == 0 else second for index in range(size))
        else:
            nums = tuple(rng.randint(1, 1000) for _ in range(size))
        cases.add(nums)
    assert all(
        2 <= len(nums) <= 2000 and all(1 <= value <= 1000 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
