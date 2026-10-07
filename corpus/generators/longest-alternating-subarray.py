def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (2, 3, 3, 2, 2),
        (4, 5, 6, 5, 5),
        (1, 2),
        (1, 1),
        tuple(1 + i % 2 for i in range(100)),
        (10_000, 9_999),
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(1, 10_000) for _ in range(rng.randint(2, 100))))
    assert all(2 <= len(array) <= 100 for array in arrays)
    assert all(1 <= value <= 10_000 for array in arrays for value in array)
    return [f"candidate(nums={list(array)!r})" for array in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[2, 3, 4, 3, 4])",
    "candidate(nums=[4, 5, 6])",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
