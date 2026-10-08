def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(edges=[[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values=[5, 2, 5, 2, 1, 1])",
        "candidate(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[20, 10, 9, 7, 4, 3, 5])",
        f"candidate(edges={[[i, i - 1] for i in range(1, 20000)]!r}, values={[1] * 20000!r})",
    }
    while len(cases) < 600:
        n = rng.randint(2, 1000)
        edges = [[node, rng.randrange(node)] for node in range(1, n)]
        values = [rng.randint(1, 1_000_000_000) for _ in range(n)]
        assert len(edges) == n - 1 and all(0 <= a < n and 0 <= b < n for a, b in edges)
        assert len(values) == n and all(1 <= value <= 1_000_000_000 for value in values)
        cases.add(f"candidate(edges={edges!r}, values={values!r})")
    return sorted(cases)
