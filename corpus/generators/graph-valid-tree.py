import random


def generate(seed: int = 0) -> list[str]:
    """Generate simple undirected graphs with valid endpoint indices, including trees and cycles."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 30
        edges = []
        if i % 2 == 0:
            for node in range(1, n):
                edges.append([node, rng.randrange(node)])
        else:
            pool = [(a, b) for a in range(n) for b in range(a + 1, n)]
            rng.shuffle(pool)
            edges = [list(x) for x in pool[: min(len(pool), i % 40)]]
        call = f"candidate(n={n}, edges={edges!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
