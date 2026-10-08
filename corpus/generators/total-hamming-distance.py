import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (0,),
        (0, 1),
        (10**9 - 1, 10**9),
        (4, 14, 2),
        (1, 1, 1, 1),
        tuple(i % 2 for i in range(10_000)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        mode = rng.randrange(3)
        if mode == 0:
            nums = tuple(rng.randint(0, 10**9) for _ in range(n))
        elif mode == 1:
            mask = rng.randint(0, 10**9)
            nums = tuple(mask if rng.random() < 0.5 else 10**9 - mask for _ in range(n))
        else:
            nums = tuple(rng.choice((0, 1, 2, 3, 2**29, 10**9)) for _ in range(n))
        cases.add(nums)
    assert all(
        1 <= len(nums) <= 10_000 and all(0 <= x <= 10**9 for x in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
