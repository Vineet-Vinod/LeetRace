def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(grid=[[1, 0], [0, 1]])", "candidate(grid=[[1, 0], [1, 1]])"]
    )
    for index in range(600):
        rows, cols = (
            (250, 250) if index % 100 == 0 else (1 + index % 15, 1 + (index * 7) % 15)
        )
        grid = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(grid={grid!r})")
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        grid = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
