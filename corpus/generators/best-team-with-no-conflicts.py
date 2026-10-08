import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((1, 3, 5, 10, 15), (1, 2, 3, 4, 5)),
        ((4, 5, 6, 5), (2, 1, 2, 1)),
        ((1, 2, 3, 5), (8, 9, 10, 1)),
    }
    cases.add((tuple(1 for _ in range(1000)), tuple(1 for _ in range(1000))))
    cases.add((tuple(1_000_000 for _ in range(1000)), tuple(1000 for _ in range(1000))))
    while len(cases) < 600:
        size = rng.randint(1, 80)
        cases.add(
            (
                tuple(rng.randint(1, 10**6) for _ in range(size)),
                tuple(rng.randint(1, 1000) for _ in range(size)),
            )
        )
    assert all(
        1 <= len(scores) <= 1000
        and len(scores) == len(ages)
        and all(1 <= score <= 10**6 for score in scores)
        and all(1 <= age <= 1000 for age in ages)
        for scores, ages in cases
    )
    return [
        f"candidate(scores={list(scores)!r}, ages={list(ages)!r})"
        for scores, ages in sorted(cases)
    ]
