import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    positive = {tuple(sorted(((0, 0), (40000, 0), (0, 40000), (40000, 40000))))}
    negative = {tuple((i, i) for i in range(500))}
    while len(positive) < 300:
        x1, x2 = sorted(rng.sample(range(0, 40001), 2))
        y1, y2 = sorted(rng.sample(range(0, 40001), 2))
        points = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        while len(points) < rng.randint(4, 50):
            points.add((rng.randint(0, 40000), rng.randint(0, 40000)))
        positive.add(tuple(sorted(points)))
    while len(negative) < 300:
        n = rng.randint(4, 50)
        xs = sorted(rng.sample(range(0, 40001), n))
        ys = sorted(rng.sample(range(0, 40001), n))
        negative.add(tuple(zip(xs, ys)))
    calls = []
    for points in sorted(positive | negative):
        calls.append(f"candidate(points={[list(point) for point in points]!r})")
    calls.append(
        "candidate(points=[[0,0],[40000,0],[0,40000],[40000,40000]]+[ [i,i] for i in range(4,500)])"
    )
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    assert all(
        1 <= len(points) <= 500
        and len(points) == len(set(points))
        and all(0 <= x <= 40000 and 0 <= y <= 40000 for x, y in points)
        for points in positive | negative
    )
    return calls
