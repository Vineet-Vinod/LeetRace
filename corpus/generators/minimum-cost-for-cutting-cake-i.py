def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(1, 20), rng.randint(1, 20)
        h = [rng.randint(1, 1000) for _ in range(m - 1)]
        v = [rng.randint(1, 1000) for _ in range(n - 1)]
        cases.add(f"candidate(m={m},n={n},horizontalCut={h!r},verticalCut={v!r})")
    return sorted(cases)
