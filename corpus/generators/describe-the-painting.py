import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[int, int, int], ...]] = set()

    def add(segments: list[list[int]]) -> None:
        key = tuple(map(tuple, segments))
        if key not in seen:
            assert 1 <= len(segments) <= 20_000
            assert all(1 <= start < end <= 100_000 for start, end, _ in segments)
            colors = [color for _, _, color in segments]
            assert all(1 <= color <= 10**9 for color in colors)
            assert len(colors) == len(set(colors))
            seen.add(key)
            cases.append(f"candidate(segments={segments!r})")

    add([[1, 4, 5], [4, 7, 7], [1, 7, 9]])
    add([[1, 7, 9], [6, 8, 15], [8, 10, 7]])
    add([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]])
    # Both neighboring spans sum to seven, but their mixed color sets differ.
    add([[1, 2, 2], [1, 2, 5], [2, 3, 3], [2, 3, 4]])
    add([[start, start + 1, start] for start in range(1, 20_001)])

    while len(cases) < 600:
        count = rng.randint(1, 20)
        starts = rng.sample(range(1, 100), count)
        segments = []
        for color, start in enumerate(starts, 1):
            end = rng.randint(start + 1, 110)
            segments.append([start, end, color])
        add(segments)
    return cases
