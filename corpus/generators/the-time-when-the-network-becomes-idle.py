def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(edges=[[0, 1], [1, 2]], patience=[0, 2, 1])",
        "candidate(edges=[[0, 1], [0, 2], [1, 2]], patience=[0, 10, 10])",
    }
    n = 100000
    chain = [[i, i + 1] for i in range(n - 1)]
    patience = [0] + [100000] * (n - 1)
    cases.add(f"candidate(edges={chain!r}, patience={patience!r})")
    while len(cases) < 600:
        n = rng.randint(2, 35)
        edges = [[i, i + 1] for i in range(n - 1)]
        for a in range(n):
            for b in range(a + 2, n):
                if rng.random() < 0.04:
                    edges.append([a, b])
        rng.shuffle(edges)
        patience = [0] + [rng.randint(1, 100000) for _ in range(n - 1)]
        assert 2 <= n <= 100000 and len(edges) <= min(100000, n * (n - 1) // 2)
        assert len({tuple(sorted(e)) for e in edges}) == len(edges) and all(
            0 <= a < n and 0 <= b < n and a != b for a, b in edges
        )
        cases.add(f"candidate(edges={edges!r}, patience={patience!r})")
    return sorted(cases)
