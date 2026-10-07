def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase[:8]) for _ in range(rng.randint(1, 300))
        )
        words = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 50))
            )
            for _ in range(rng.randint(1, 100))
        ]
        cases.add(f"candidate(s={s!r}, words={words!r})")
    return sorted(cases)
