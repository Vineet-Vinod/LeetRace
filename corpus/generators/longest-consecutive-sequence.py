import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (),
        (100, 4, 200, 1, 3, 2),
        (0, 3, 7, 2, 5, 8, 4, 6, 0, 1),
        (1, 0, 1, 2),
        tuple(range(-50000, 50000)),
        (-(10**9), 10**9),
    }
    while len(cases) < 600:
        if rng.random() < 0.55:
            start = rng.randint(-(10**9), 10**9 - 100)
            length = rng.randint(1, 100)
            nums = list(range(start, start + length))
            rng.shuffle(nums)
            cases.add(tuple(nums))
        else:
            cases.add(
                tuple(rng.randint(-(10**9), 10**9) for _ in range(rng.randint(0, 100)))
            )
    assert len(cases) == 600 and all(
        len(a) <= 100000 and all(-(10**9) <= v <= 10**9 for v in a) for a in cases
    )
    return [f"candidate(nums={list(a)!r})" for a in sorted(cases)]
