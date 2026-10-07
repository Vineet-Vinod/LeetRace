def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    positive_max = [[value, 0] for value in range(1, 5001)]
    positive_max += [[-value, 0] for value in range(1, 5001)]
    negative_max = [[value, 0] for value in range(-4999, 5000)]
    negative_max.append([100000000, 100000000])
    cases = {
        f"candidate(points={positive_max!r})",
        f"candidate(points={negative_max!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            center = rng.randint(-1000, 1000)
            pairs = rng.randint(1, 25)
            points = []
            for _ in range(pairs):
                x = rng.randint(-10000, 10000)
                y = rng.randint(-10000, 10000)
                points.extend([[x, y], [2 * center - x, y]])
            if rng.random() < 0.5:
                points.append([center, rng.randint(-10000, 10000)])
        else:
            points = [
                [rng.randint(-1000, 1000), rng.randint(-1000, 1000)]
                for _ in range(rng.randint(1, 50))
            ]
            points.append([100000000, 100000000])
        assert 1 <= len(points) <= 10000
        assert all(
            -100000000 <= value <= 100000000 for point in points for value in point
        )
        cases.add(f"candidate(points={points!r})")
    return sorted(cases)
