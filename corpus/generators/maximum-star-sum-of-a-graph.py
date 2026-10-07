def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 50)
        vals = [rng.randint(-10000, 10000) for _ in range(n)]
        all_edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(all_edges)
        edges = [list(x) for x in all_edges[: rng.randint(0, min(len(all_edges), 100))]]
        k = rng.randint(0, n - 1)
        cases.add(f"candidate(vals={vals!r},edges={edges!r},k={k})")
    return sorted(cases)
