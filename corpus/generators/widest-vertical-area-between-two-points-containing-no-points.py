import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        ((8, 7), (9, 9), (7, 4), (9, 7)),
        ((3, 1), (9, 0), (1, 0), (1, 4), (5, 3), (8, 8)),
    }
    cases.add(
        tuple(
            (rng.randint(0, 1_000_000_000), rng.randint(0, 1_000_000_000))
            for _ in range(100_000)
        )
    )
    cases.add(
        ((0, 0), (1_000_000_000, 1_000_000_000))
        + tuple((i, i) for i in range(1, 99_999))
    )
    while len(cases) < 600:
        size = rng.randint(2, 200)
        cases.add(
            tuple(
                (rng.randint(0, 1_000_000_000), rng.randint(0, 1_000_000_000))
                for _ in range(size)
            )
        )
    return [f"candidate(points={[[x, y] for x, y in points]!r})" for points in cases]
