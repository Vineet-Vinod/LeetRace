def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 20)
        a = [[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        b = [[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        cases.add(f"candidate(img1={a!r},img2={b!r})")
    return sorted(cases)
