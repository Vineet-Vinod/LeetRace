def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(start=[1, 1], target=[4, 5], specialRoads=[[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]])",
        "candidate(start=[3, 2], target=[5, 7], specialRoads=[[5, 7, 3, 2, 1], [3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]])",
        "candidate(start=[1, 1], target=[10, 4], specialRoads=[[4, 2, 1, 1, 3], [1, 2, 7, 4, 4], [10, 3, 6, 1, 2], [6, 1, 1, 2, 3]])",
        "candidate(start=[1, 1], target=[5, 5], specialRoads=[[1, 1, 5, 5, 20]])",
        "candidate(start=[1, 1], target=[8, 8], specialRoads=[[1, 2, 4, 4, 2], [4, 4, 8, 8, 3]])",
        "candidate(start=[2, 2], target=[9, 6], specialRoads=[[3, 2, 6, 4, 2], [6, 4, 9, 6, 2], [2, 2, 5, 5, 10]])",
        "candidate(start=[1, 1], target=[6, 6], specialRoads=[[2, 2, 3, 3, 1], [3, 3, 4, 4, 1], [4, 4, 5, 5, 1], [5, 5, 6, 6, 1]])",
        "candidate(start=[5, 5], target=[7, 9], specialRoads=[[5, 6, 7, 7, 1], [7, 7, 7, 9, 5], [6, 5, 7, 9, 4]])",
        f"candidate(start={[1, 1]!r}, target={[100000, 100000]!r}, specialRoads={[[i, i, i + 1, i + 1, 100000] for i in range(1, 201)]!r})",
    }
    while len(cases) < 600:
        start_x, start_y = rng.randint(1, 1000), rng.randint(1, 1000)
        target_x = rng.randint(start_x, 100_000)
        target_y = rng.randint(start_y, 100_000)
        roads = [
            [
                rng.randint(start_x, target_x),
                rng.randint(start_y, target_y),
                rng.randint(start_x, target_x),
                rng.randint(start_y, target_y),
                rng.randint(1, 100_000),
            ]
            for _ in range(rng.randint(1, 20))
        ]
        assert len(roads) <= 200
        assert all(
            start_x <= x1 <= target_x
            and start_x <= x2 <= target_x
            and start_y <= y1 <= target_y
            and start_y <= y2 <= target_y
            and 1 <= cost <= 100_000
            for x1, y1, x2, y2, cost in roads
        )
        cases.add(
            f"candidate(start={[start_x, start_y]!r}, target={[target_x, target_y]!r}, specialRoads={roads!r})"
        )
    return sorted(cases)
