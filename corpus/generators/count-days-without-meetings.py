import random


def generate(seed: int = 0) -> list[str]:
    """Generate valid inclusive meeting intervals, both overlapping and disjoint."""
    rng = random.Random(seed)
    boundary = [[2 * day, 2 * day] for day in range(1, 100_001)]
    overlapping_boundary = [[1, 1_000_000_000]] * 100_000
    calls = [
        "candidate(days=1000000000, meetings=[[1, 1], [1000000000, 1000000000]])",
        f"candidate(days=1000000000, meetings={boundary!r})",
        f"candidate(days=1000000000, meetings={overlapping_boundary!r})",
    ]
    seen: set[str] = set(calls)
    index = 0
    while len(calls) < 600:
        days = 1 + index % 200
        meeting_count = 1 + index % 16
        meetings: list[list[int]] = []
        if index % 2:
            next_day = 1
            while len(meetings) < meeting_count and next_day <= days:
                start = rng.randint(next_day, days)
                end = rng.randint(start, days)
                meetings.append([start, end])
                next_day = end + 1
        else:
            for _ in range(meeting_count):
                start = rng.randint(1, days)
                end = rng.randint(start, days)
                meetings.append([start, end])
        assert 1 <= len(meetings) <= 100_000
        assert all(1 <= start <= end <= days for start, end in meetings)
        call = f"candidate(days={days}, meetings={meetings!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
