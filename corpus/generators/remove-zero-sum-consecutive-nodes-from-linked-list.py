import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    inputs: set[tuple[int, ...]] = {
        (1, 2, -3, 3, 1),
        (1, 2, 3, -3, 4),
        (1, 2, 3, -3, -2),
        (1,) * 1000,
        (1, -1) * 500,
        (1000,) * 1000,
    }
    while len(inputs) < 600:
        family = len(inputs) % 3
        if family == 0:
            values = tuple(rng.randint(-1000, 1000) for _ in range(rng.randint(1, 100)))
        elif family == 1:
            prefix = [rng.randint(-20, 20) for _ in range(rng.randint(1, 40))]
            values = tuple(prefix + [-sum(prefix)])
        else:
            values = tuple(rng.randint(1, 1000) for _ in range(rng.randint(1, 100)))
        if 1 <= len(values) <= 1000 and all(-1000 <= value <= 1000 for value in values):
            inputs.add(values)
    assert all(1 <= len(values) <= 1000 for values in inputs)
    assert all(-1000 <= value <= 1000 for values in inputs for value in values)
    calls = [
        f"candidate(head=list_node({list(values)!r}))" for values in sorted(inputs)
    ]
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    return calls
