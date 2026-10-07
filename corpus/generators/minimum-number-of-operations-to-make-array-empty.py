import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (3, 3, 4, 3, 4),
        (2, 1, 2, 2, 3, 3),
        (1, 1),
        (1, 1, 1),
        (5, 5, 5, 5),
        (1000000, 1000000),
    }
    while len(cases) < 600:
        nums = []
        values = rng.randint(2, 8)
        make_possible = rng.random() < 0.5
        singleton = rng.randint(1, values) if not make_possible else 0
        for value in range(1, values + 1):
            count = 1 if value == singleton else rng.choice((2, 3, 4, 5, 6, 7))
            nums.extend([value] * count)
        rng.shuffle(nums)
        cases.add(tuple(nums))
    assert len(cases) == 600 and all(
        2 <= len(a) <= 100000 and all(1 <= v <= 10**6 for v in a) for a in cases
    )
    return [f"candidate(nums={list(a)!r})" for a in sorted(cases)]
