def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        vals = [rng.randint(1, 10**9) for _ in range(n)]
        cases.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(cases)
