import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (2, 1),
        (2,),
        (5, 1, 2, 4, 3),
        (1,),
        (3, 6, 9),
        (10_000,) * 100_000,
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10_000) for _ in range(rng.randint(1, 100))))
    assert all(
        1 <= len(stones) <= 100_000 and all(1 <= value <= 10_000 for value in stones)
        for stones in cases
    )
    return [f"candidate(stones={list(stones)!r})" for stones in sorted(cases)]
