def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)

    def valid_values(count: int) -> list[int]:
        values = []
        start = 0
        level = 0
        width = 1
        while start < count:
            size = min(width, count - start)
            if level % 2 == 0:
                values.extend(1 + 2 * index for index in range(size))
            else:
                values.extend(2 * (width - index) for index in range(size))
            start += size
            width *= 2
            level += 1
        return values

    cases = set()
    for count in [1, 2, 3, 7, 15, 31, 100, 255, 1023, 100000]:
        values = valid_values(count)
        cases.add(f"candidate(root=tree_node({values!r}))")
        if count > 1:
            broken = values.copy()
            broken[count // 2] += 1
            cases.add(f"candidate(root=tree_node({broken!r}))")
    while len(cases) < 600:
        count = rng.randint(1, 100)
        if rng.random() < 0.5:
            values = valid_values(count)
            cases.add(f"candidate(root=tree_node({values!r}))")
        else:
            values = [rng.randint(1, 10**6) for _ in range(count)]
            cases.add(f"candidate(root=tree_node({values!r}))")
    assert len(cases) == 600
    return sorted(cases)
