def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        width = rng.randint(1, 1000)
        books = [[rng.randint(1, width), rng.randint(1, 1000)] for _ in range(n)]
        cases.add(f"candidate(books={books!r}, shelfWidth={width})")
    return sorted(cases)
