import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 50)
        graph = [set() for _ in range(n)]
        for u in range(n):
            for v in range(u + 1, n):
                if rng.random() < 0.08:
                    graph[u].add(v)
                    graph[v].add(u)
        adjacency = [sorted(neighbors) for neighbors in graph]
        calls.add(f"candidate(graph={adjacency!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])",
    "candidate(graph=[[1, 3], [0, 2], [1, 3], [0, 2]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
