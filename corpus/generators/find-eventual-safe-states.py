def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(graph=[[]])"}
    while len(cases) < 600:
        n = rng.randint(2, 30)
        graph = []
        for i in range(n):
            graph.append(sorted(j for j in range(n) if rng.random() < 0.08))
        if not any(graph):
            graph[0] = [1]
        cases.add(f"candidate(graph={graph!r})")
    return sorted(cases)
