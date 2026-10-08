import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        ((1, 2), (2, 3), (3, 4), (1, 3)),
        ((1, 2), (1, 2), (1, 2)),
        ((1, 2), (2, 3)),
        ((-50_000, 50_000),),
    }
    cases.add(tuple((0, 1) for _ in range(100_000)))
    while len(cases) < 600:
        intervals = []
        for _ in range(rng.randint(1, 70)):
            start = rng.randint(-50_000, 49_999)
            intervals.append((start, rng.randint(start + 1, 50_000)))
        cases.add(tuple(intervals))
    assert all(
        1 <= len(intervals) <= 100_000
        and all(-50_000 <= start < end <= 50_000 for start, end in intervals)
        for intervals in cases
    )
    return [
        f"candidate(intervals={[[start, end] for start, end in intervals]!r})"
        for intervals in sorted(cases)
    ]
