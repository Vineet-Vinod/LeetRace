import random


def _call(values: list[int]) -> str:
    middle = len(values) // 2
    expected_node = "h" + ".next" * middle
    suffix = values[middle:]
    return (
        f"(lambda h: (lambda result: (result is {expected_node}, "
        f"is_same_list(result, list_node({suffix!r}))))(candidate(head=h)))"
        f"(list_node({values!r}))"
    )


def generate(seed: int = 0) -> list[str]:
    """List size and values are both in [1, 100]; returned-node identity is asserted."""
    rng = random.Random(seed)
    cases = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1], [100] * 100]
    seen = {tuple(values) for values in cases}
    while len(cases) < 600:
        values = [rng.randint(1, 100) for _ in range(rng.randint(1, 100))]
        key = tuple(values)
        if key not in seen:
            seen.add(key)
            cases.append(values)

    assert len(cases) == 600
    assert all(1 <= len(values) <= 100 for values in cases)
    assert all(1 <= value <= 100 for values in cases for value in values)
    return [_call(values) for values in cases]
