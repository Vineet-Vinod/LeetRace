def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(cells=[0,1,0,1,1,0,0,1],n=7)"}
    while len(cases) < 600:
        cells = [rng.randrange(2) for _ in range(8)]
        n = rng.randint(1, 10**9)
        cases.add(f"candidate(cells={cells!r},n={n})")
    return sorted(cases)
