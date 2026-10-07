import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        edges = []
        for a in range(n):
            for b in range(a + 1, n):
                if rng.random() < 0.08:
                    edges.append([a, b, rng.randint(1, 100000)])
        disappear = [rng.randint(1, 100000) for _ in range(n)]
        key = (n, tuple(map(tuple, edges)), tuple(disappear))
        if key not in seen:
            seen.add(key)
            assert len(disappear) == n and all(1 <= v <= 100000 for v in disappear)
            assert all(0 <= a < b < n and 1 <= w <= 100000 for a, b, w in edges)
            cases.append(f"candidate(n={n}, edges={edges!r}, disappear={disappear!r})")
    return cases
