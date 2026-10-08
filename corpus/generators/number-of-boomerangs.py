def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(points=[[0, 0]])",
        "candidate(points=[[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]])",
        "candidate(points=[[0, 0], [1, 0], [2, 0], [3, 0]])",
        "candidate(points=[[0, 0], [3, 4], [-3, 4], [3, -4], [-3, -4]])",
        f"candidate(points={[[value, 0] for value in range(-250, 250)]!r})",
    }

    while len(cases) < 350:
        size = rng.randint(3, 80)
        step = rng.randint(1, 20)
        max_offset = 10000 - (size - 1) * step
        offset = rng.randint(-10000, max_offset)
        if rng.random() < 0.5:
            points = [[offset + index * step, 0] for index in range(size)]
        else:
            points = [[0, offset + index * step] for index in range(size)]
        assert len(points) == len({tuple(point) for point in points})
        assert all(
            -10000 <= coordinate <= 10000 for point in points for coordinate in point
        )
        cases.add(f"candidate(points={points!r})")

    while len(cases) < 600:
        size = rng.randint(1, 40)
        points = set()
        while len(points) < size:
            points.add((rng.randint(-10000, 10000), rng.randint(-10000, 10000)))
        values = [list(point) for point in points]
        assert len(values) == len({tuple(point) for point in values})
        cases.add(f"candidate(points={values!r})")
    assert len(cases) == 600
    return sorted(cases)
