def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 30)
        price = [rng.randint(0, 1000) for _ in range(n)]
        taste = [rng.randint(0, 1000) for _ in range(n)]
        amount = rng.randint(0, 1000)
        coupons = rng.randint(0, 5)
        cases.add(
            f"candidate(price={price!r}, tastiness={taste!r}, maxAmount={amount}, maxCoupons={coupons})"
        )
    return sorted(cases)
