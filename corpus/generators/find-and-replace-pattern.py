def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 20)
        pattern = "".join(rng.choice(string.ascii_lowercase) for _ in range(n))
        words = [
            "".join(rng.choice(string.ascii_lowercase) for _ in range(n))
            for _ in range(rng.randint(1, 50))
        ]
        cases.add(f"candidate(words={words!r}, pattern={pattern!r})")
    return sorted(cases)
