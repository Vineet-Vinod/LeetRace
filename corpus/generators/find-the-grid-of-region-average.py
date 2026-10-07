def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(3, 15), rng.randint(3, 15)
        image = [[rng.randint(0, 255) for _ in range(n)] for _ in range(m)]
        threshold = rng.randint(0, 255)
        cases.add(f"candidate(image={image!r}, threshold={threshold})")
    return sorted(cases)
