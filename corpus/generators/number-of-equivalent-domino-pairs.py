import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        ((1, 2), (2, 1), (3, 4), (5, 6)),
        ((1, 2), (1, 2), (1, 1)),
    }
    cases.add(((9, 9),) * 40_000)
    while len(cases) < 600:
        size = rng.randint(1, 200)
        cases.add(tuple((rng.randint(1, 9), rng.randint(1, 9)) for _ in range(size)))
    cases.add(tuple((rng.randint(1, 9), rng.randint(1, 9)) for _ in range(40_000)))
    calls = [f"candidate(dominoes={[[a, b] for a, b in values]!r})" for values in cases]
    calls.extend(["candidate(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])"])
    return list(dict.fromkeys(calls))
