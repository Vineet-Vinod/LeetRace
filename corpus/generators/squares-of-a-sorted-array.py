import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (-4, -1, 0, 3, 10),
        (-7, -3, 2, 3, 11),
        tuple(range(-5000, 5000)),
    }
    cases.add(tuple(range(-10_000, 0)))
    cases.add((-10_000, 0, 10_000))
    while len(cases) < 600:
        cases.add(
            tuple(
                sorted(rng.randint(-10_000, 10_000) for _ in range(rng.randint(1, 200)))
            )
        )
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
