import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (),
        (0, 1, 2, 4, 5, 7),
        (0, 2, 3, 4, 6, 8, 9),
        (-(1 << 31), (1 << 31) - 1),
    }
    cases.add(tuple(range(-10, 10)))
    while len(cases) < 600:
        values = rng.sample(range(-1_000_000, 1_000_001), rng.randint(0, 20))
        cases.add(tuple(sorted(values)))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
