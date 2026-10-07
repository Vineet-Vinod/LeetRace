def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])"])
    for index in range(600):
        n = 2 + index % 1000
        if index == 0:
            n = 100000
        edges = []
        for source in range(n):
            for destination in range(source + 1, min(n, source + 1 + (index % 3))):
                if rng.random() < 0.35:
                    edges.append([source, destination])
        if not edges:
            edges = [[0, 1]]
        cases.add(f"candidate(n={n}, edges={edges!r})")
    return sorted(cases)
