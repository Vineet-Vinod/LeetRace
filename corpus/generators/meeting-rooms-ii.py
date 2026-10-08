import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        ((0, 30), (5, 10), (15, 20)),
        ((2, 4), (7, 10)),
        ((0, 1), (1, 2)),
        ((0, 10), (0, 10), (0, 10)),
    }
    cases.add(tuple((2 * i, 2 * i + 1) for i in range(10_000)))
    while len(cases) < 600:
        intervals = []
        for _ in range(rng.randint(1, 60)):
            start = rng.randint(0, 999_998)
            intervals.append((start, rng.randint(start + 1, 1_000_000)))
        cases.add(tuple(intervals))
    assert all(
        1 <= len(intervals) <= 10_000
        and all(0 <= start < end <= 1_000_000 for start, end in intervals)
        for intervals in cases
    )
    return [
        f"candidate(intervals={[[start, end] for start, end in intervals]!r})"
        for intervals in sorted(cases)
    ]
