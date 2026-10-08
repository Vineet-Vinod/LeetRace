import random

EXAMPLES = [
    "candidate(points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1])",
    "candidate(points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1])",
    "candidate(points=[[1, 0], [2, 1]], angle=13, location=[1, 1])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(points, angle, location):
        assert 1 <= len(points) <= 100000 and 0 <= angle < 360 and len(location) == 2
        assert all(
            len(p) == 2 and all(0 <= v <= 100 for v in p) for p in points + [location]
        )
        emit(f"candidate(points={points!r}, angle={angle}, location={location!r})")

    add([[i % 101, (i // 101) % 101] for i in range(100000)], 359, [50, 50])
    add([[50, 50]] * 100000, 0, [50, 50])
    for angle in [0, 45, 90, 180, 270, 359]:
        add(
            [[50, 50], [100, 50], [50, 100], [0, 50], [50, 0], [100, 100], [0, 0]],
            angle,
            [50, 50],
        )
    while len(calls) < 600:
        location = [rng.randint(0, 100), rng.randint(0, 100)]
        points = [
            [rng.randint(0, 100), rng.randint(0, 100)]
            for _ in range(rng.randint(1, 50))
        ]
        if rng.random() < 0.4:
            points.extend([location[:]] * rng.randint(1, 5))
        if rng.random() < 0.3:
            points.extend([rng.choice(points)[:]] * rng.randint(1, 5))
        add(
            points, rng.choice([0, 45, 90, 180, 270, 359, rng.randrange(360)]), location
        )
    return calls
