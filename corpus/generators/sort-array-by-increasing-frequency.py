def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (1, 1, 2, 2, 2, 3),
        (2, 3, 1, 3, 2),
        (-1, 1, -6, 4, 5, -6, 1, 4, 1),
        tuple(i % 201 - 100 for i in range(100)),
        (-100, 100),
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(-100, 100) for _ in range(rng.randint(1, 100))))
    calls = [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]
    assert all(1 <= len(array) <= 100 for array in arrays)
    assert all(-100 <= value <= 100 for array in arrays for value in array)
    return calls


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[1, 1, 2, 2, 2, 3])",
    "candidate(nums=[2, 3, 1, 3, 2])",
    "candidate(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1])",
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
