def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = 2 * rng.randint(1, 500)
        opens = n // 2
        chars = ["["] * opens + ["]"] * opens
        rng.shuffle(chars)
        cases.add(f"candidate(s={''.join(chars)!r})")
    return sorted(cases)
