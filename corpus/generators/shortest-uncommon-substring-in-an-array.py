def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 100)
        arr = [
            "".join(
                rng.choice(string.ascii_lowercase[:8])
                for _ in range(rng.randint(1, 20))
            )
            for _ in range(n)
        ]
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
