import random


def generate(seed: int = 0) -> list[str]:
    """Generate transitively closed, asymmetric DAGs with unique and multiple sources; n is 1..100."""
    rng = random.Random(seed)
    calls = {
        "candidate(n=3, edges=[[0, 1], [1, 2], [0, 2]])",
        "candidate(n=4, edges=[[0, 2], [1, 3], [1, 2]])",
        "candidate(n=1, edges=[])",
        "candidate(n=100, edges=[[i, j] for i in range(100) for j in range(i + 1, 100)])",
        "candidate(n=100, edges=[[i, j] for i in range(2, 100) for j in range(i + 1, 100)] + [[0, j] for j in range(2, 100)] + [[1, j] for j in range(2, 100)])",
    }
    while len(calls) < 600:
        n = rng.randint(2, 30)
        order = list(range(n))
        rng.shuffle(order)
        unique_source = rng.random() < 0.55
        if unique_source:
            edges = [[order[i], order[j]] for i in range(n) for j in range(i + 1, n)]
        else:
            edges = [[order[i], order[j]] for i in range(2, n) for j in range(i + 1, n)]
            edges.extend([[order[0], order[j]] for j in range(2, n)])
            edges.extend([[order[1], order[j]] for j in range(2, n)])
        edges.sort()
        assert 1 <= n <= 100
        edge_set = {(u, v) for u, v in edges}
        position = {team: index for index, team in enumerate(order)}
        assert all(u != v and position[u] < position[v] for u, v in edge_set)
        assert all(
            (order[i], order[j]) in edge_set
            for i in range(n)
            for j in range(i + 1, n)
            if unique_source or i >= 2 or j >= 2
        )
        calls.add(f"candidate(n={n}, edges={edges!r})")
    return sorted(calls)
