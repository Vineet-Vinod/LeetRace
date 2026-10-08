import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 2, 3, 10, 4, 2, 3, 5),
        (5, 4, 3, 2, 1),
        (1, 2, 3),
        (1,),
        (2, 2, 2),
    }
    cases.update((tuple(range(100_000)), (10**9,) * 100_000))
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 10**9) for _ in range(rng.randint(1, 100))))
    assert all(
        1 <= len(arr) <= 100_000 and all(0 <= value <= 10**9 for value in arr)
        for arr in cases
    )
    return [f"candidate(arr={list(arr)!r})" for arr in sorted(cases)]
