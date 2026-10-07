def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(n=4, roads=[[1, 2, 4], [2, 3, 2], [2, 4, 5]], appleCost=[56, 42, 102, 301], k=2)",
            "candidate(n=1000, roads=[[i, i + 1, 1] for i in range(1, 1000)] + [[i, i + 2, 2] for i in range(1, 999)] + [[i, i + 3, 3] for i in range(1, 4)], appleCost=[100000] * 1000, k=100)",
        ]
    )
    for index in range(600):
        n = 2 + index % 100
        edges = [[node, node + 1, rng.randint(1, 100000)] for node in range(1, n)]
        possible = {(edge[0], edge[1]) for edge in edges}
        for _ in range(min(n, 20)):
            first, second = sorted(rng.sample(range(1, n + 1), 2))
            if (first, second) not in possible:
                edges.append([first, second, rng.randint(1, 100000)])
                possible.add((first, second))
        apples = [rng.randint(1, 100000) for _ in range(n)]
        k = rng.randint(1, 100)
        cases.add(f"candidate(n={n}, roads={edges!r}, appleCost={apples!r}, k={k})")
    return sorted(cases)
