def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        vals = [rng.randint(0, 100) for _ in range(n)]
        k = rng.randint(1, n)
        cases.add(f"candidate(head=list_node({vals!r}), k={k})")
    return sorted(cases)
