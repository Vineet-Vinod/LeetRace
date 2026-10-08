import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    boundary = [[2 * index, 2 * index + 1] for index in range(10000)]
    attendable: set[str] = {f"candidate(intervals={boundary!r})"}
    overlapping: set[str] = set()

    while len(attendable) < 300:
        intervals = []
        start = rng.randint(0, 1000)
        for _ in range(rng.randint(0, 100)):
            if start >= 999999:
                break
            end = min(1000000, start + rng.randint(1, 100))
            intervals.append([start, end])
            start = min(1000000, end + rng.randint(0, 100))
        assert all(0 <= left < right <= 1000000 for left, right in intervals)
        assert all(
            intervals[i - 1][1] <= intervals[i][0] for i in range(1, len(intervals))
        )
        attendable.add(f"candidate(intervals={intervals!r})")

    while len(overlapping) < 300:
        start = rng.randint(0, 999998)
        first_end = rng.randint(start + 1, min(1000000, start + 100))
        second_start = rng.randint(start, first_end - 1)
        second_end = rng.randint(first_end, min(1000000, second_start + 100))
        intervals = [[start, first_end], [second_start, second_end]]
        for _ in range(rng.randint(0, 20)):
            extra_start = rng.randint(0, 999999)
            extra_end = rng.randint(extra_start + 1, 1000000)
            intervals.append([extra_start, extra_end])
        assert all(0 <= left < right <= 1000000 for left, right in intervals)
        assert any(
            intervals[i][0] < intervals[j][1] and intervals[j][0] < intervals[i][1]
            for i in range(len(intervals))
            for j in range(i + 1, len(intervals))
        )
        overlapping.add(f"candidate(intervals={intervals!r})")

    return sorted(attendable | overlapping)
