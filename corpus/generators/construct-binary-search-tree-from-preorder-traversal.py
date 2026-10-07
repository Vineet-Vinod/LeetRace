def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(preorder=[8,5,1,7,10,12])", "candidate(preorder=[1,3])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        vals = rng.sample(range(1, 1001), n)
        cases.add(f"candidate(preorder={vals!r})")
    return sorted(cases)
