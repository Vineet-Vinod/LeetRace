def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        points = []
        distances = set()
        while len(points) < rng.randint(1, 20):
            point = [rng.randint(-10000, 10000), rng.randint(-10000, 10000)]
            distance = point[0] * point[0] + point[1] * point[1]
            if point not in points and distance not in distances:
                points.append(point)
                distances.add(distance)
        k = rng.randint(1, len(points))
        assert len({tuple(point) for point in points}) == len(points)
        assert len(distances) == len(points)
        cases.add(f"candidate(points={points!r}, k={k})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = (
        f"candidate(points={[[index, 0] for index in range(1, 10001)]!r}, k=5000)"
    )
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
