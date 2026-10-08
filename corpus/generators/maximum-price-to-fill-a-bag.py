def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(items: list[list[int]], capacity: int) -> None:
        assert 1 <= len(items) <= 100_000
        assert all(
            len(item) == 2 and 1 <= item[0] <= 10_000 and 1 <= item[1] <= 10_000
            for item in items
        )
        assert 1 <= capacity <= 1_000_000_000
        cases.add(f"candidate(items={items!r}, capacity={capacity})")

    # Full size, full item-value bounds, and feasible exact/partial fills.
    add([[10_000, 10_000]] * 100_000, 10_000)
    add([[10_000, 1], [1, 10_000]], 5_000)
    add([[1, 1]], 1)
    add([[10_000, 1]], 2)
    add([[1, 1]], 1_000_000_000)
    add([[7, 3], [11, 4]], 7)
    add([[7, 3], [11, 4]], 8)

    # Explicitly balance feasible capacities against capacities beyond all stock.
    for index in range(250):
        size = 1 + index % 30
        items = [[rng.randint(1, 10_000), rng.randint(1, 10_000)] for _ in range(size)]
        total_weight = sum(weight for _, weight in items)
        capacity = rng.randint(1, total_weight)
        add(items, capacity)

    for index in range(250):
        size = 1 + index % 30
        items = [[rng.randint(1, 10_000), rng.randint(1, 10_000)] for _ in range(size)]
        total_weight = sum(weight for _, weight in items)
        add(items, total_weight + 1)

    while len(cases) < 600:
        size = rng.randint(1, 100)
        items = [[rng.randint(1, 10_000), rng.randint(1, 10_000)] for _ in range(size)]
        total_weight = sum(weight for _, weight in items)
        if rng.random() < 0.5:
            capacity = rng.randint(1, total_weight)
        else:
            capacity = total_weight + 1
        add(items, capacity)

    result = list(cases)
    rng.shuffle(result)
    return result
