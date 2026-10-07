import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: DAG, n 2..15, unique valid edges; generated edge sets use increasing labels."""
    rng = random.Random(seed)
    calls: set[str] = set()
    fixed = [[[1, 2], [3], [3], []], [[1], []], [[1, 2, 3], [], [], []]]
    for graph in fixed:
        calls.add(f"candidate(graph={graph!r})")
    while len(calls) < 600:
        n = rng.randint(2, 9)
        graph = [[] for _ in range(n)]
        # Edges only go to larger labels, so every generated graph is a DAG.
        for node in range(n - 1):
            for neighbor in range(node + 1, n):
                if rng.random() < 0.24:
                    graph[node].append(neighbor)
        if not graph[0]:
            graph[0].append(n - 1)
        # Ensure every edge list is unique and node n-1 has no outgoing edges.
        calls.add(f"candidate(graph={graph!r})")
    return sorted(calls)
