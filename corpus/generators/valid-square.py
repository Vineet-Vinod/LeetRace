import random


def _is_square(points: tuple[tuple[int, int], ...]) -> bool:
    distances = sorted(
        (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        for i in range(4)
        for j in range(i + 1, 4)
    )
    return (
        distances[0] > 0
        and distances[:4] == [distances[0]] * 4
        and distances[4:] == [2 * distances[0]] * 2
    )


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    square_cases = {
        tuple(
            sorted(((-10000, -10000), (10000, -10000), (-10000, 10000), (10000, 10000)))
        ),
        tuple(sorted(((0, -10000), (10000, 0), (0, 10000), (-10000, 0)))),
    }
    nonsquare_cases = set()
    while len(square_cases) < 300:
        x, y = rng.randint(-5000, 5000), rng.randint(-5000, 5000)
        a, b = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
        if a == b == 0:
            continue
        points = ((x, y), (x + a, y + b), (x + a - b, y + b + a), (x - b, y + a))
        key = tuple(sorted(points))
        if all(
            -10000 <= coordinate <= 10000 for point in points for coordinate in point
        ):
            square_cases.add(key)
    while len(nonsquare_cases) < 300:
        points = tuple(
            (rng.randint(-10000, 10000), rng.randint(-10000, 10000)) for _ in range(4)
        )
        if len(set(points)) != 4 or _is_square(points):
            continue
        nonsquare_cases.add(tuple(sorted(points)))
    calls = []
    for points in sorted(square_cases | nonsquare_cases):
        shuffled = list(points)
        rng.shuffle(shuffled)
        calls.append(
            f"candidate(p1={list(shuffled[0])!r}, p2={list(shuffled[1])!r}, p3={list(shuffled[2])!r}, p4={list(shuffled[3])!r})"
        )
    assert len(calls) == 600 and len(calls) == len(set(calls))
    assert all(
        len(points) == 4
        and all(-10000 <= x <= 10000 and -10000 <= y <= 10000 for x, y in points)
        for points in square_cases | nonsquare_cases
    )
    assert all(_is_square(points) for points in square_cases)
    assert all(not _is_square(points) for points in nonsquare_cases)
    return calls
