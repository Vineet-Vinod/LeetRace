def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        row_count = rng.randint(1, 12)
        width = rng.randint(1, 30)
        shared = rng.randint(1, 10000) if rng.random() < 0.7 else None
        rows = []
        for _ in range(row_count):
            row = set()
            if shared is not None:
                row.add(shared)
            while len(row) < width:
                row.add(rng.randint(1, 10000))
            rows.append(sorted(row))
        assert all(row == sorted(set(row)) and len(row) == width for row in rows)
        cases.add(f"candidate(mat={rows!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
