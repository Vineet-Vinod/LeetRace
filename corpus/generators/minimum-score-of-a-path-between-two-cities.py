def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edges = []
        for node in range(2, n + 1):
            edges.append([node, rng.randint(1, node - 1), rng.randint(1, 10000)])
        existing = {(min(a, b), max(a, b)) for a, b, _ in edges}
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if (a, b) not in existing and rng.random() < 0.08:
                    edges.append([a, b, rng.randint(1, 10000)])
        cases.add(f"candidate(n={n},roads={edges!r})")
    return sorted(cases)
