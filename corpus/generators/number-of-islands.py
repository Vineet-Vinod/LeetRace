def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(grid=[['1']])"}
    while len(cases) < 600:
        r, c = rng.randint(1, 30), rng.randint(1, 30)
        grid = [[rng.choice(["0", "1"]) for _ in range(c)] for _ in range(r)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
