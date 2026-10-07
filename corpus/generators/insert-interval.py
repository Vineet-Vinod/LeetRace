def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        count = rng.randint(0, 30)
        intervals = []
        position = rng.randint(0, 100)
        for _ in range(count):
            start = position + rng.randint(1, 10)
            end = min(100000, start + rng.randint(0, 100))
            intervals.append([start, end])
            position = end
        start = rng.randint(0, 100000)
        end = rng.randint(start, 100000)
        assert all(
            intervals[i][1] < intervals[i + 1][0] for i in range(len(intervals) - 1)
        )
        cases.add(f"candidate(intervals={intervals!r}, newInterval={[start, end]!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(intervals={[[2 * index, 2 * index + 1] for index in range(10000)]!r}, newInterval=[-1, 20001])"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
