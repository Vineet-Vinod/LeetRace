import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1,),
        (1, 3, 5, 4, 7),
        (2, 2, 2, 2, 2),
        tuple(range(-5000, 5000)),
    }
    cases.add(tuple(range(-1_000_000_000, -999_990_000)))
    cases.add((-1_000_000_000, 1_000_000_000))
    while len(cases) < 600:
        cases.add(
            tuple(
                rng.randint(-1_000_000_000, 1_000_000_000)
                for _ in range(rng.randint(1, 200))
            )
        )
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
