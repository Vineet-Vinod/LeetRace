def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n, k = rng.randint(1, 6), rng.randint(1, 6)
        composition = [[rng.randint(1, 100) for _ in range(n)] for _ in range(k)]
        stock = [rng.randint(0, 10**8) for _ in range(n)]
        cost = [rng.randint(1, 100) for _ in range(n)]
        budget = rng.randint(0, 10**8)
        cases.add(
            f"candidate(n={n}, k={k}, budget={budget}, composition={composition!r}, stock={stock!r}, cost={cost!r})"
        )
    return sorted(cases)
