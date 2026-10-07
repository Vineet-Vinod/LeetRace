def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        queries = [
            "".join(rng.choice(string.ascii_lowercase[:8]) for _ in range(n))
            for _ in range(rng.randint(1, 100))
        ]
        dictionary = [
            "".join(rng.choice(string.ascii_lowercase[:8]) for _ in range(n))
            for _ in range(rng.randint(1, 100))
        ]
        cases.add(f"candidate(queries={queries!r}, dictionary={dictionary!r})")
    return sorted(cases)
