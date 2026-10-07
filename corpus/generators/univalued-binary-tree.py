import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty binary trees with both uniform and mixed node values."""
    rng = random.Random(seed)
    true_cases = set()
    false_cases = set()

    while len(true_cases) < 300:
        count = rng.randint(1, 100)
        value = rng.randint(0, 99)
        true_cases.add(tuple([value] * count))
    while len(false_cases) < 300:
        count = rng.randint(2, 100)
        values = [rng.randint(0, 99) for _ in range(count)]
        if values[1] == values[0]:
            values[1] = (values[0] + 1) % 100
        false_cases.add(tuple(values))

    cases = (
        true_cases
        | false_cases
        | {
            (1, 1, 1, 1, 1, None, 1),
            (2, 2, 2, 5, 2),
        }
    )
    calls = [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
    boundary = tuple([99] * 100)
    calls.append(f"candidate(root=tree_node({list(boundary)!r}))")
    return calls
