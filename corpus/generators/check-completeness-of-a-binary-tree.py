def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(root=tree_node([1, 2, 3, 4, 5, 6]))",
        "candidate(root=tree_node([1, 2, 3, 4, 5, None, 7]))",
    }
    for index in range(600):
        size = 1 + index % 100
        values = [rng.randint(1, 1000) for _ in range(size)]
        if index % 2 and size > 2:
            values[rng.randrange(2, size)] = None
        cases.add(f"candidate(root=tree_node({values!r}))")
    while len(cases) < 600:
        values = [rng.randint(1, 1000) for _ in range(rng.randint(1, 100))]
        if rng.random() < 0.5 and len(values) > 2:
            values[rng.randrange(2, len(values))] = None
        cases.add(f"candidate(root=tree_node({values!r}))")
    return sorted(cases)
