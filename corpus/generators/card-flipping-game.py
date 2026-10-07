def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(fronts=[1],backs=[1])"}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        f = [rng.randint(1, 30) for _ in range(n)]
        b = [rng.randint(1, 30) for _ in range(n)]
        cases.add(f"candidate(fronts={f!r},backs={b!r})")
    return sorted(cases)
