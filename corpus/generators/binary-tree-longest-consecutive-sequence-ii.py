def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(values: list[int | None]) -> None:
        while values and values[-1] is None:
            values.pop()
        assert values and values[0] is not None
        assert len(values) <= 30_000
        assert all(value is None or -30_000 <= value <= 30_000 for value in values)
        for child in range(1, len(values)):
            parent = (child - 1) // 2
            assert values[parent] is not None or values[child] is None
        cases.add(f"candidate(root=tree_node({values!r}))")

    add([rng.randint(-30_000, 30_000) for _ in range(30_000)])
    add([1])
    add([1, 2, 3])
    add([2, 1, 3])
    add([0, -1, 1, -2, None, None, 2, -3, None, None, None, None, None, None, 3])
    add([0, 1, None, 2, None, None, None, 3])
    add(
        [
            0,
            1,
            None,
            2,
            None,
            None,
            None,
            3,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            4,
        ]
    )

    # Perfect small trees put increasing and decreasing arms around the root,
    # exercising long child-parent-child paths with both orientations.
    for depth in range(2, 7):
        size = (1 << (depth + 1)) - 1
        for peak in (-depth, 0, depth):
            values: list[int | None] = [
                rng.randint(-30_000, 30_000) for _ in range(size)
            ]
            values[0] = peak
            left = 0
            right = 0
            for step in range(1, depth + 1):
                left = 2 * left + 1
                right = 2 * right + 2
                values[left] = peak - step
                values[right] = peak + step
            add(values)

    # General trees retain the full value range, with enough structured parent
    # values to create a mixture of consecutive and non-consecutive edges.
    for index in range(580):
        size = 1 + index % 50
        values: list[int | None] = [rng.randint(-30_000, 30_000) for _ in range(size)]
        for child in range(1, size):
            if rng.random() < 0.12:
                values[child] = None
            elif rng.random() < 0.15 and values[(child - 1) // 2] is not None:
                values[child] = values[(child - 1) // 2] + rng.choice((-1, 1))
        for child in range(1, len(values)):
            parent = (child - 1) // 2
            if values[parent] is None:
                values[child] = None
        if values[0] is None:
            values[0] = rng.randint(-30_000, 30_000)
        add(values)

    result = list(cases)
    rng.shuffle(result)
    return result
