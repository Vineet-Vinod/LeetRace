def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(memory1=2, memory2=2)"}
    while len(cases) < 600:
        a, b = rng.randint(0, 2**31 - 1), rng.randint(0, 2**31 - 1)
        cases.add(f"candidate(memory1={a}, memory2={b})")
    return sorted(cases)
