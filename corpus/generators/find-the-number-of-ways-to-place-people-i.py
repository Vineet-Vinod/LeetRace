import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 1), (2, 2), (3, 3)),
        ((6, 2), (4, 4), (2, 6)),
        ((3, 1), (1, 3), (1, 1)),
    }
    all_points = [(x, y) for x in range(51) for y in range(51)]
    while len(cases) < 600:
        n = rng.randint(2, 50)
        points = tuple(rng.sample(all_points, n))
        cases.add(points)
    return [
        f"candidate(points={[list(point) for point in points]!r})" for points in cases
    ]
