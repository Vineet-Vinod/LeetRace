import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        n = rng.randint(2, 60)
        edges = []
        for a in range(n):
            for b in range(a + 1, n):
                if rng.random() < 0.06:
                    edges.append([a, b])
        key = (n, tuple(map(tuple, edges)))
        if key not in seen:
            seen.add(key)
            assert (
                all(0 <= a < b < n for a, b in edges) and len(edges) <= n * (n - 1) // 2
            )
            cases.append(f"candidate(n={n}, edges={edges!r})")
    return cases
