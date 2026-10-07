def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(piles=[5, 4, 9], k=2)",
        f"candidate(piles={[10000] * 100000!r}, k=100000)",
    }
    while len(cases) < 600:
        piles = [rng.randint(1, 10_000) for _ in range(rng.randint(1, 1000))]
        k = rng.randint(1, 1000)
        assert 1 <= len(piles) <= 100_000 and all(1 <= x <= 10_000 for x in piles)
        assert 1 <= k <= 100_000
        cases.add(f"candidate(piles={piles!r}, k={k})")
    return sorted(cases)
