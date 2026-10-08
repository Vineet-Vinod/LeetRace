def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        height = rng.randint(1, 7)
        size = 2**height - 1
        values = [rng.randint(0, 10**5) for _ in range(size)]
        assert size == 2**height - 1
        cases.add(f"candidate(root=tree_node({values!r}))")
    assert len(cases) >= 500
    return sorted(cases)[:600]
