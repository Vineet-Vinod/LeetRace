import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1,),
        (5, 3, 4, 1, 1),
        (6, 5, 3, 9, 2, 7),
        (3, 2, 5, 5, 2, 3),
    }
    while len(cases) < 600:
        n = rng.randint(1, 45)
        cases.add(tuple(rng.randint(1, 10**9) for _ in range(n)))
    return [f"candidate(heights={list(heights)!r})" for heights in cases]
