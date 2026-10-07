import random


def _area_twice(points: list[list[int]]) -> int:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    true_cases: set[str] = set()
    false_cases: set[str] = set()

    while len(true_cases) < 300:
        points = [
            list(point)
            for point in rng.sample([(x, y) for x in range(101) for y in range(101)], 3)
        ]
        if _area_twice(points) == 0:
            continue
        assert len(set(map(tuple, points))) == 3
        assert all(0 <= coordinate <= 100 for point in points for coordinate in point)
        true_cases.add(f"candidate(points={points!r})")

    while len(false_cases) < 300:
        if rng.randrange(2):
            point = [rng.randint(0, 100), rng.randint(0, 100)]
            other = [rng.randint(0, 100), rng.randint(0, 100)]
            points = [point, point.copy(), other]
        elif rng.randrange(2):
            x = rng.randint(0, 100)
            ys = rng.sample(range(101), 3)
            points = [[x, y] for y in ys]
        else:
            y = rng.randint(0, 100)
            xs = rng.sample(range(101), 3)
            points = [[x, y] for x in xs]
        assert len(points) == 3 and all(
            0 <= coordinate <= 100 for point in points for coordinate in point
        )
        assert _area_twice(points) == 0
        false_cases.add(f"candidate(points={points!r})")

    assert not true_cases & false_cases
    return sorted(true_cases | false_cases)
