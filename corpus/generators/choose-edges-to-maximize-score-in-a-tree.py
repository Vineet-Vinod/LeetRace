def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(edges=[[-1,-1]])"}
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edges = [[-1, -1]]
        for node in range(1, n):
            edges.append([rng.randrange(node), rng.randint(-100, 100)])
        cases.add(f"candidate(edges={edges!r})")
    return sorted(cases)
