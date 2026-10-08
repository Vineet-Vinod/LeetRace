import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (2, 3, 1, 6, 7),
        (1, 1, 1, 1, 1),
        (1,),
        (1,) * 300,
        (10**8,) * 300,
        (1, 2) * 150,
        (1, 2, 3) * 100,
    }
    while len(cases) < 600:
        if rng.random() < 0.75:
            arr = tuple(rng.randint(1, 15) for _ in range(rng.randint(1, 100)))
        else:
            arr = tuple(rng.randint(1, 10**8) for _ in range(rng.randint(1, 100)))
        cases.add(arr)
    assert all(
        1 <= len(arr) <= 300 and all(1 <= value <= 10**8 for value in arr)
        for arr in cases
    )
    return [f"candidate(arr={list(arr)!r})" for arr in sorted(cases)]
