def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        points = [
            [rng.randint(0, 500), rng.randint(0, 500)]
            for _ in range(rng.randint(1, 30))
        ]
        queries = [
            [rng.randint(0, 500), rng.randint(0, 500), rng.randint(1, 500)]
            for _ in range(rng.randint(1, 30))
        ]
        cases.add(f"candidate(points={points!r},queries={queries!r})")
    return sorted(cases)
