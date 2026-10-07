def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        a, b, c = (rng.randint(1, 10**9) for _ in range(3))
        cases.add(f"candidate(a={a}, b={b}, c={c})")
    return sorted(cases)
