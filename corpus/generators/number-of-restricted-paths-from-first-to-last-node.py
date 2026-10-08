def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 80)
        edge_map = {}
        for v in range(1, n):
            edge_map[(v, rng.randrange(v))] = rng.randint(1, 10**5)
        extra = (
            rng.randint(0, min(100, n * (n - 1) // 2 - len(edge_map))) if n > 2 else 0
        )
        available = [
            (a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in edge_map
        ]
        for a, b in rng.sample(available, extra):
            edge_map[(a, b)] = rng.randint(1, 10**5)
        edges = [[a + 1, b + 1, w] for (a, b), w in edge_map.items()]
        cases.add(f"candidate(n={n}, edges={edges!r})")
    return sorted(cases)
