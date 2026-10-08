import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(2, 80)
        edges = []
        for node in range(1, n):
            edges.append([node, rng.randrange(node)])
        rng.shuffle(edges)
        key = tuple(map(tuple, edges))
        if key not in seen:
            seen.add(key)
            assert len(edges) == n - 1 and all(
                0 <= a < b < n or 0 <= b < a < n for a, b in edges
            )
            cases.append(f"candidate(edges={edges!r})")
    return cases
