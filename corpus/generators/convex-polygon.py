import random


_MAX_POINTS = 10_000
_COORD_LIMIT = 10_000


def generate(seed: int = 0) -> list[str]:
    """Generate simple polygons with unique vertices, original coordinate limits, and a 10,000-point boundary."""
    rng = random.Random(seed)
    side = 2500
    maximum = (
        [[x, 0] for x in range(side)]
        + [[side, y] for y in range(side)]
        + [[x, side] for x in range(side, 0, -1)]
        + [[0, y] for y in range(side, 0, -1)]
    )
    boundary = [[-_COORD_LIMIT, 0], [_COORD_LIMIT, 0], [0, _COORD_LIMIT]]
    cases = {
        "candidate(points=[[0, 0], [0, 5], [5, 5], [5, 0]])",
        "candidate(points=[[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]])",
        f"candidate(points={maximum!r})",
        f"candidate(points={boundary!r})",
    }
    while len(cases) < 600:
        width = rng.randint(4, 2000)
        height = rng.randint(4, 2000)
        if rng.random() < 0.5:
            points = [[0, 0], [0, height], [width, height], [width, 0]]
        else:
            notch_x = rng.randint(1, width - 1)
            notch_y = rng.randint(1, height - 1)
            points = [
                [0, 0],
                [0, height],
                [width, height],
                [width, 0],
                [notch_x, notch_y],
            ]
        cases.add(f"candidate(points={points!r})")

    assert len(cases) == 600
    return sorted(cases)
