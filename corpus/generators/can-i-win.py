def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        f"candidate(maxChoosableInteger={m}, desiredTotal={total})"
        for m in range(18, 21)
        for total in (0, 1, m * (m + 1) // 2 // 2, m * (m + 1) // 2, 300)
    }
    while len(cases) < 600:
        maximum = rng.randint(1, 16)
        total = rng.randint(0, 300)
        cases.add(f"candidate(maxChoosableInteger={maximum}, desiredTotal={total})")
    return sorted(cases)
