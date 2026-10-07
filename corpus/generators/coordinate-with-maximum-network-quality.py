import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int, int], ...], int]] = {
        (((1, 2, 5), (2, 1, 7), (3, 1, 9)), 2),
        (((23, 11, 21),), 9),
        (((1, 2, 13), (2, 1, 7), (0, 1, 9)), 2),
    }
    cases.add((tuple((i + 1, i, 50) for i in range(50)), 50))
    while len(cases) < 600:
        towers = tuple(
            (x, y, rng.randint(0, 50))
            for x, y in rng.sample(
                [(x, y) for x in range(51) for y in range(51)], rng.randint(1, 10)
            )
        )
        cases.add((towers, rng.randint(1, 50)))
    assert all(
        1 <= len(towers) <= 50
        and 1 <= radius <= 50
        and len({(x, y) for x, y, _ in towers}) == len(towers)
        and all(
            0 <= x <= 50 and 0 <= y <= 50 and 0 <= quality <= 50
            for x, y, quality in towers
        )
        for towers, radius in cases
    )
    return [
        f"candidate(towers={[list(t) for t in towers]!r}, radius={radius})"
        for towers, radius in sorted(cases)
    ]
