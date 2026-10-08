def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(root=tree_node([10, 5, 15, 1, 8, None, 7]))",
            "candidate(root=tree_node([]))",
        ]
    )
    for index in range(600):
        size = 10000 if index == 0 else index % 200
        if size == 0:
            values = []
        else:
            values = [rng.randint(-10000, 10000) for _ in range(size)]
            for position in range(1, len(values)):
                if rng.random() < 0.1:
                    values[position] = None
            while values and values[-1] is None:
                values.pop()
            for position in range(1, len(values)):
                if values[(position - 1) // 2] is None:
                    values[position] = None
        cases.add(f"candidate(root=tree_node({values!r}))")
    while len(cases) < 600:
        values = [rng.randint(-10000, 10000) for _ in range(rng.randint(0, 200))]
        cases.add(f"candidate(root=tree_node({values!r}))")
    return sorted(cases)
