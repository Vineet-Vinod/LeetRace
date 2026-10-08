def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(costs=[17,12,10,2,7,2,11,20,8],k=3,candidates=4)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        costs = [rng.randint(1, 1000) for _ in range(n)]
        k = rng.randint(1, n)
        candidates = rng.randint(1, n)
        cases.add(f"candidate(costs={costs!r},k={k},candidates={candidates})")
    return sorted(cases)
