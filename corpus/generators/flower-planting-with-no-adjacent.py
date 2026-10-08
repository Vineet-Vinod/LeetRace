def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=3,paths=[[1,2],[2,3],[3,1]])"}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        edges = []
        degree = [0] * n
        for node in range(1, n):
            options = [p for p in range(node) if degree[p] < 3]
            if options and rng.random() < 0.8:
                parent = rng.choice(options)
                edges.append([parent + 1, node + 1])
                degree[parent] += 1
                degree[node] += 1
        cases.add(f"candidate(n={n},paths={edges!r})")
    return sorted(cases)
