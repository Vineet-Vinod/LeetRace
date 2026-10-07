import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, tuple[tuple[int, int], ...]]] = {
        (6, ((0, 1), (1, 3), (2, 3), (4, 0), (4, 5))),
        (5, ((1, 0), (1, 2), (3, 2), (3, 4))),
        (3, ((1, 0), (2, 0))),
    }
    cases.add((50_000, tuple((0, node) for node in range(1, 50_000))))
    while len(cases) < 600:
        n = rng.randint(2, 80)
        edges = []
        for node in range(1, n):
            parent = rng.randrange(node)
            edge = (parent, node) if rng.random() < 0.5 else (node, parent)
            edges.append(edge)
        rng.shuffle(edges)
        cases.add((n, tuple(edges)))
    assert all(
        2 <= n <= 50_000
        and len(edges) == n - 1
        and len({frozenset(edge) for edge in edges}) == len(edges)
        and all(0 <= a < n and 0 <= b < n and a != b for a, b in edges)
        for n, edges in cases
    )
    return [
        f"candidate(n={n}, connections={[[a, b] for a, b in edges]!r})"
        for n, edges in sorted(cases)
    ]
