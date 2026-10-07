def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        r, c = 2 * rng.randint(0, 7) + 1, 2 * rng.randint(0, 7) + 1
        grid = [sorted(rng.randint(1, 10**6) for _ in range(c)) for _ in range(r)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
