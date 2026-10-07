import random


def generate(seed: int = 0) -> list[str]:
    """Generate simple undirected graphs: no loops or repeated edges, endpoints are in range."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 25
        edges = []
        for a in range(n):
            for b in range(a + 1, n):
                if rng.random() < 0.12:
                    edges.append([a, b])
        assert all(a < b and 0 <= a < b < n for a, b in edges) and len(
            {(a, b) for a, b in edges}
        ) == len(edges)
        call = f"candidate(n={n}, edges={edges!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
