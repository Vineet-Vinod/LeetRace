def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(label=14)", "candidate(label=26)"}
    while len(cases) < 600:
        label = rng.randint(1, 10**6)
        cases.add(f"candidate(label={label})")
    return sorted(cases)
