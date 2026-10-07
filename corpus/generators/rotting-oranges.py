def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        rows, cols = rng.randint(1, 10), rng.randint(1, 10)
        grid = [[rng.randint(0, 2) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(grid={grid!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
