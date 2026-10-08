def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 500)
        vals = [rng.randint(-500, 500) for _ in range(n)]
        left = rng.randint(1, n)
        right = rng.randint(left, n)
        cases.add(f"candidate(head=list_node({vals!r}), left={left}, right={right})")
    return sorted(cases)
