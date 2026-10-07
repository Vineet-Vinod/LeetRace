def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        values = [rng.randint(1, 20) for _ in range(rng.randint(1, 100))]
        target = rng.randint(1, 20)
        cases.add(f"candidate(root=tree_node({values!r}), target={target})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
