def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        values = [rng.randint(-(2**31), 2**31 - 1) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(root=tree_node({values!r}))")
    assert len(cases) >= 500
    return sorted(cases)[:600]
