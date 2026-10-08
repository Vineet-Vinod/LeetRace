import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((1, 2, 2, 1), (3, 1, 2), (1, 3, 2), (2, 4), (3, 1, 2), (1, 3, 1, 1)),
        ((1,), (1,), (1,)),
        ((5,),),
    }
    cases.add(tuple((1,) for _ in range(10_000)))
    while len(cases) < 600:
        rows = rng.randint(1, 30)
        width = rng.randint(1, 200)
        wall = []
        for _ in range(rows):
            cuts = (
                sorted(rng.sample(range(1, width), rng.randint(0, min(12, width - 1))))
                if width > 1
                else []
            )
            points = [0, *cuts, width]
            wall.append(
                tuple(points[i + 1] - points[i] for i in range(len(points) - 1))
            )
        cases.add(tuple(wall))
    assert all(
        1 <= len(wall) <= 10_000
        and 1 <= len(wall[0]) <= 10_000
        and all(
            sum(row) == sum(wall[0]) and all(brick > 0 for brick in row) for row in wall
        )
        and sum(map(len, wall)) <= 20_000
        for wall in cases
    )
    return [
        f"candidate(wall={[list(row) for row in wall]!r})" for wall in sorted(cases)
    ]
