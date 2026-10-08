def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])"}

    def add(intervals: list[list[int]]) -> None:
        assert 1 <= len(intervals) <= 10_000
        assert all(
            len(interval) == 2 and 0 <= interval[0] <= interval[1] <= 10_000
            for interval in intervals
        )
        cases.add(f"candidate(intervals={intervals!r})")

    add([[index, index] for index in range(10_000)])
    while len(cases) < 600:
        size = rng.randint(1, 100)
        intervals = []
        for _ in range(size):
            start = rng.randint(0, 10_000)
            intervals.append([start, rng.randint(start, 10_000)])
        add(intervals)
    for call in cases:
        eval(call, {"candidate": add})
    return sorted(cases)
