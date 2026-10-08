import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]] = {
        (((0, 0), (2, 1)), ((1, 2), (3, 3))),
        (((0, 0), (1, 0), (2, 0)), ((0, 1), (2, 1), (3, 0), (3, 1))),
        (tuple((i, 0) for i in range(5)), tuple((i, 999) for i in range(5))),
    }
    cases.add((tuple((i, 0) for i in range(10)), tuple((i, 999) for i in range(10))))
    while len(cases) < 600:
        workers_count = rng.randint(1, 7)
        bike_count = rng.randint(workers_count, 8)
        points = rng.sample(
            [(x, y) for x in range(30) for y in range(30)], workers_count + bike_count
        )
        cases.add((tuple(points[:workers_count]), tuple(points[workers_count:])))
    assert all(
        1 <= len(workers) <= len(bikes) <= 10
        and len(set(workers)) == len(workers)
        and len(set(bikes)) == len(bikes)
        and all(0 <= x < 1000 and 0 <= y < 1000 for x, y in workers + bikes)
        for workers, bikes in cases
    )
    return [
        f"candidate(workers={[list(p) for p in workers]!r}, bikes={[list(p) for p in bikes]!r})"
        for workers, bikes in sorted(cases)
    ]
