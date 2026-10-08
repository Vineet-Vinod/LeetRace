def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        vals = [rng.randint(-5000, 5000) for _ in range(rng.randint(1, 500))]
        vals.sort(key=abs)
        cases.add(f"candidate(head=list_node({vals!r}))")
    return sorted(cases)
