def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 300))
        )
        k = rng.randint(1, len(s))
        cases.add(f"candidate(s={s!r}, k={k})")
    return sorted(cases)
