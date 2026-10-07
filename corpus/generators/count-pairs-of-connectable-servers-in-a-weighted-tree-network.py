def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edges = []
        for node in range(1, n):
            edges.append([node, rng.randrange(node), rng.randint(1, 1000)])
        speed = rng.randint(1, 1000)
        cases.add(f"candidate(edges={edges!r},signalSpeed={speed})")
    return sorted(cases)
