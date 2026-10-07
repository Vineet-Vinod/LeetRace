def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        values = set()
        while len(values) < rng.randint(1, 30):
            start = rng.randint(0, 99999)
            end = rng.randint(start + 1, 100000)
            values.add((start, end))
        intervals = [list(value) for value in values]
        assert len(intervals) == len({tuple(interval) for interval in intervals})
        cases.add(f"candidate(intervals={intervals!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = (
        f"candidate(intervals={[[index, 2001 - index] for index in range(1000)]!r})"
    )
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
