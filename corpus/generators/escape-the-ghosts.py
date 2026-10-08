import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], tuple[int, int]]] = {
        (((1, 0), (0, 3)), (0, 1)),
        (((1, 0),), (2, 0)),
        (((2, 0),), (1, 0)),
        (((0, 0),), (0, 0)),
        (((10_000, -10_000),), (10_000, 10_000)),
    }
    cases.add((tuple((-10_000, -10_000) for _ in range(100)), (10_000, 10_000)))
    while len(cases) < 600:
        target = (rng.randint(-10_000, 10_000), rng.randint(-10_000, 10_000))
        ghosts = tuple(
            (rng.randint(-10_000, 10_000), rng.randint(-10_000, 10_000))
            for _ in range(rng.randint(1, 10))
        )
        cases.add((ghosts, target))
    assert all(
        1 <= len(ghosts) <= 100
        and all(-10_000 <= x <= 10_000 and -10_000 <= y <= 10_000 for x, y in ghosts)
        and -10_000 <= target[0] <= 10_000
        and -10_000 <= target[1] <= 10_000
        for ghosts, target in cases
    )
    return [
        f"candidate(ghosts={[[x, y] for x, y in ghosts]!r}, target={list(target)!r})"
        for ghosts, target in sorted(cases)
    ]
