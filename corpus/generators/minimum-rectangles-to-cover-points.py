import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], int]] = {
        (((2, 1), (1, 0), (1, 4), (1, 8), (3, 5), (4, 6)), 1),
        (tuple((x, x) for x in range(7)), 2),
        (((2, 3), (1, 2)), 0),
        (tuple((x, x % 17) for x in range(100_000)), 0),
        (((10**9, 10**9), (0, 0)), 10**9),
    }
    while len(cases) < 600:
        width = rng.randint(0, 100)
        groups = rng.randint(1, 30)
        points: set[tuple[int, int]] = set()
        for group in range(groups):
            left = group * (width + rng.randint(1, 20))
            for _ in range(rng.randint(1, 5)):
                x = min(10**9, left + rng.randint(0, width))
                y = rng.randint(0, 10**9)
                points.add((x, y))
        cases.add((tuple(points), width))
    assert all(
        1 <= len(points) <= 100_000
        and 0 <= w <= 10**9
        and len(set(points)) == len(points)
        and all(0 <= x <= 10**9 and 0 <= y <= 10**9 for x, y in points)
        for points, w in cases
    )
    return [
        f"candidate(points={[list(point) for point in points]!r}, w={w})"
        for points, w in sorted(cases)
    ]
