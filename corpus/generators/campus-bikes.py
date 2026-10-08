def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 10)
        m = rng.randint(n, 15)
        pts = rng.sample([(x, y) for x in range(30) for y in range(30)], n + m)
        w, b = pts[:n], pts[n:]
        cases.add(f"candidate(workers={w!r},bikes={b!r})")
    return sorted(cases)
