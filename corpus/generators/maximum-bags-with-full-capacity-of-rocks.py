def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        capacity = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        rocks = [rng.randint(0, c) for c in capacity]
        add = rng.randint(1, 10**9)
        cases.add(
            f"candidate(capacity={capacity!r}, rocks={rocks!r}, additionalRocks={add})"
        )
    return sorted(cases)
