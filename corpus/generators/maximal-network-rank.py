def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 30)
        all_edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(all_edges)
        roads = [list(edge) for edge in all_edges[: rng.randint(0, len(all_edges))]]
        cases.add(f"candidate(n={n},roads={roads!r})")
    return sorted(cases)
