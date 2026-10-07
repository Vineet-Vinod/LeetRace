import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        n = rng.randint(2, 25)
        edges = []
        for node in range(2, n + 1):
            parent = rng.randint(1, node - 1)
            edges.append([node, parent, rng.randint(0, 100000)])
        pairs = {(min(a, b), max(a, b)) for a, b, _ in edges}
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if (a, b) not in pairs and rng.random() < 0.08:
                    edges.append([a, b, rng.randint(0, 100000)])
        rng.shuffle(edges)
        key = (n, tuple(map(tuple, edges)))
        if key not in seen:
            seen.add(key)
            assert len(edges) >= n - 1 and all(
                1 <= a < n + 1 and 1 <= b <= n and a != b for a, b, _ in edges
            )
            cases.append(f"candidate(n={n}, connections={edges!r})")
    return cases
