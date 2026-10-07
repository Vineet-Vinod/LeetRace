def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(ranks=[4,2,3,1],cars=10)"}
    while len(cases) < 600:
        n = rng.randint(1, 50)
        ranks = [rng.randint(1, 100) for _ in range(n)]
        cars = rng.randint(1, 10000)
        cases.add(f"candidate(ranks={ranks!r},cars={cars})")
    return sorted(cases)
