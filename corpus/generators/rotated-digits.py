def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=1)", "candidate(n=10)"}
    while len(cases) < 600:
        cases.add(f"candidate(n={rng.randint(1, 10000)})")
    return sorted(cases)
