def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 500)
        arr = [rng.randint(0, 10**9) for _ in range(n)]
        k = rng.randint(1, n)
        cases.add(f"candidate(arr={arr!r}, k={k})")
    return sorted(cases)
