def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 10**6)
        limit = rng.randint(1, 10**6)
        cases.add(f"candidate(n={n},limit={limit})")
    return sorted(cases)
