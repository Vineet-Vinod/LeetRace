import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (3, 2, 3),
        (1,),
        (1, 2),
        (2, 2, 1, 1, 1, 2, 2),
        (5,) * 100,
        (5,) * 17 + (8,) * 17 + (9,) * 16,
        tuple(range(1, 50_001)),
        (-(10**9), 10**9),
        (10**9,),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        mode = rng.randrange(3)
        if mode == 0:
            value = rng.randint(-(10**9), 10**9)
            nums = (value,) * (size // 2 + 1) + tuple(
                rng.randint(-(10**9), 10**9) for _ in range(size // 2)
            )
        elif mode == 1 and size >= 3:
            first, second = rng.sample(range(-1000, 1001), 2)
            nums = (first,) * (size // 3 + 1) + (second,) * (size // 3 + 1)
            nums += tuple(rng.randint(-(10**9), 10**9) for _ in range(size - len(nums)))
        else:
            nums = tuple(rng.randint(-(10**9), 10**9) for _ in range(size))
        cases.add(tuple(nums))
    assert all(
        1 <= len(nums) <= 50_000 and all(-(10**9) <= x <= 10**9 for x in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
