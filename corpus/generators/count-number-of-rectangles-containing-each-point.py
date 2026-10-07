def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nr, np = rng.randint(1, 40), rng.randint(1, 40)
        rectangles = set()
        while len(rectangles) < nr:
            rectangles.add((rng.randint(1, 10**9), rng.randint(1, 100)))
        points = set()
        while len(points) < np:
            points.add((rng.randint(1, 10**9), rng.randint(1, 100)))
        cases.add(
            f"candidate(rectangles={list(map(list, rectangles))!r}, points={list(map(list, points))!r})"
        )
    return sorted(cases)
