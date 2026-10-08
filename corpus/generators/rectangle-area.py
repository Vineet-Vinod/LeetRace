def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        ax1, ay1, bx1, by1 = [rng.randint(-(10**4), 10**4) for _ in range(4)]
        ax2 = rng.randint(ax1, 10**4)
        ay2 = rng.randint(ay1, 10**4)
        bx2 = rng.randint(bx1, 10**4)
        by2 = rng.randint(by1, 10**4)
        cases.add(
            f"candidate(ax1={ax1}, ay1={ay1}, ax2={ax2}, ay2={ay2}, bx1={bx1}, by1={by1}, bx2={bx2}, by2={by2})"
        )
    return sorted(cases)
