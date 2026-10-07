import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[tuple[tuple[int, int], ...], int]] = set()

    def add(clips: list[list[int]], time: int) -> None:
        key = (tuple(map(tuple, clips)), time)
        if key not in seen:
            assert 1 <= len(clips) <= 100
            assert 1 <= time <= 100
            assert all(0 <= start <= end <= 100 for start, end in clips)
            seen.add(key)
            cases.append(f"candidate(clips={clips!r}, time={time})")

    add([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)
    add([[0, 1], [1, 2]], 5)
    add(
        [
            [0, 1],
            [6, 8],
            [0, 2],
            [5, 6],
            [0, 4],
            [0, 3],
            [6, 7],
            [1, 3],
            [4, 7],
            [1, 4],
            [2, 5],
            [2, 6],
            [3, 4],
            [4, 5],
            [5, 7],
            [6, 9],
        ],
        9,
    )
    add([[i, i + 1] for i in range(100)], 100)
    add([[1, 100] for _ in range(100)], 100)
    add([[0, 100]] + [[i, min(100, i + 1)] for i in range(99)], 100)

    for _ in range(600):
        time = rng.randint(1, 100)
        count = rng.randint(1, 100)
        clips = []
        for _ in range(count):
            start = rng.randint(0, 100)
            end = rng.randint(start, 100)
            clips.append([start, end])
        add(clips, time)
    return cases
