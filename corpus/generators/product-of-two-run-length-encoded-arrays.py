def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        total = rng.randint(1, 100)
        a = []
        b = []

        def encode():
            result = []
            remaining = total
            while remaining:
                count = rng.randint(1, remaining)
                result.append([rng.randint(1, 10**4), count])
                remaining -= count
            return result

        a, b = encode(), encode()
        cases.add(f"candidate(encoded1={a!r}, encoded2={b!r})")
    return sorted(cases)
