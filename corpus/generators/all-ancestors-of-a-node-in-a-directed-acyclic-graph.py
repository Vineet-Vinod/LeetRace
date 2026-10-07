import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(2, 35)
        edges = []
        for a in range(n):
            for b in range(a + 1, n):
                if rng.random() < rng.uniform(0.02, 0.12):
                    edges.append([a, b])
        key = (n, tuple(map(tuple, edges)))
        if key not in seen:
            seen.add(key)
            assert all(a < b for a, b in edges)
            cases.append(f"candidate(n={n}, edges={edges!r})")
    return cases
