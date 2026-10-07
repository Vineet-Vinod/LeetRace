import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (1, 2, 2),
        (3, 2, 1, 2, 1, 7),
        (0,),
        (0, 0, 0),
        (100000,),
        tuple([0] * 100000),
    }
    while len(cases) < 600:
        if rng.random() < 0.55:
            value = rng.randint(0, 100000)
            nums = tuple([value] * rng.randint(2, 80))
        else:
            nums = tuple(rng.sample(range(100001), rng.randint(1, 100)))
        cases.add(nums)
    assert len(cases) == 600 and all(
        1 <= len(a) <= 100000 and all(0 <= v <= 100000 for v in a) for a in cases
    )
    return [f"candidate(nums={list(a)!r})" for a in sorted(cases)]
