def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    cases.add("candidate(root=tree_node([0]))")
    cases.add("candidate(root=tree_node([1]))")
    for _ in range(598):
        size = rng.randint(1, 100)
        values = [rng.randint(0, 1) for _ in range(size)]
        cases.add(f"candidate(root=tree_node({values!r}))")
    assert len(cases) >= 500
    return sorted(cases)[:600]
