def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(prices=[1])",
        "candidate(prices=[1,2,3,0,2])",
        "candidate(prices=[5,4,3,2])",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        prices = [rng.randint(0, 1000) for _ in range(n)]
        cases.add(f"candidate(prices={prices!r})")
    return sorted(cases)
