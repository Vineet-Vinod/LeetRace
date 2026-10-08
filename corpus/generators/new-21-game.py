def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        k = rng.randint(0, 10000)
        m = rng.randint(1, 10000)
        n = rng.randint(k, min(10000, k + m))
        cases.add(f"candidate(n={n}, k={k}, maxPts={m})")
    return sorted(cases)
