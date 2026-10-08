def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        rows, cols = rng.randint(1, 12), rng.randint(1, 12)
        grid = [[rng.randint(1, 100000) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(grid={grid!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
