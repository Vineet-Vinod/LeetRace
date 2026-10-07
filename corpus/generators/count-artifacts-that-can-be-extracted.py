def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        n = rng.randint(1, 30)
        cells = [(row, col) for row in range(n) for col in range(n)]
        rng.shuffle(cells)
        artifact_cells = cells[: rng.randint(1, min(len(cells), 30))]
        artifacts = [[row, col, row, col] for row, col in artifact_cells]
        dig = [[row, col] for row, col in cells if rng.random() < 0.3]
        if not dig:
            dig = [list(cells[0])]
        assert len(set(map(tuple, artifact_cells))) == len(artifact_cells)
        assert len(set(map(tuple, dig))) == len(dig)
        cases.add(f"candidate(n={n}, artifacts={artifacts!r}, dig={dig!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
