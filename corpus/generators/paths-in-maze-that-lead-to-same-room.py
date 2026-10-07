def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=3,corridors=[[1, 2], [2, 3], [1, 3]])"}
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edges = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)]
        rng.shuffle(edges)
        corridors = [list(edge) for edge in edges[: rng.randint(1, len(edges))]]
        cases.add(f"candidate(n={n},corridors={corridors!r})")
    return sorted(cases)
