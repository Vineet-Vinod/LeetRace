def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        inventory = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        orders = rng.randint(1, min(sum(inventory), 10**9))
        cases.add(f"candidate(inventory={inventory!r}, orders={orders})")
    return sorted(cases)
