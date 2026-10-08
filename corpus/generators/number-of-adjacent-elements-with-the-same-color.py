def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        q = rng.randint(1, 100)
        queries = [[rng.randrange(n), rng.randint(1, 10**5)] for _ in range(q)]
        cases.add(f"candidate(n={n}, queries={queries!r})")
    return sorted(cases)
