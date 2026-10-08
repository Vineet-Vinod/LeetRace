import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (1,),
        (1, 2, 3, 4, 5),
        (5, 4, 3, 2, 1),
        (2, 1, 5, 0, 4, 6),
        (-(2**31), 0, 2**31 - 1),
        tuple(range(500000)),
        (-(2**31), 0, 2**31 - 1),
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            start = rng.randint(-(10**6), 10**6)
            nums = tuple(start - i for i in range(rng.randint(3, 100)))
        else:
            nums = tuple(
                rng.randint(-(2**31), 2**31 - 1) for _ in range(rng.randint(1, 100))
            )
        cases.add(nums)
    assert len(cases) == 600 and all(
        1 <= len(a) <= 500000 and all(-(2**31) <= x <= 2**31 - 1 for x in a)
        for a in cases
    )
    return [f"candidate(nums={list(a)!r})" for a in sorted(cases)]
