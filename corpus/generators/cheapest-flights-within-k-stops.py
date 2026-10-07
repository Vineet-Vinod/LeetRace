def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 10)
        all_edges = [(a, b) for a in range(n) for b in range(n) if a != b]
        rng.shuffle(all_edges)
        chosen = all_edges[: rng.randint(0, min(len(all_edges), n * 2))]
        flights = [[a, b, rng.randint(1, 10000)] for a, b in chosen]
        src, dst = rng.sample(range(n), 2)
        k = rng.randint(0, n - 1)
        cases.add(f"candidate(n={n}, flights={flights!r}, src={src}, dst={dst}, k={k})")
    return sorted(cases)
