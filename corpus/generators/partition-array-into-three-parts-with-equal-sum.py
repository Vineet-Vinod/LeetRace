def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (0, 0, 0),
        (0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1),
        (1, -1, 1, -1),
        (1, 2, 3),
        (0,) * 50000,
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(-100, 100) for _ in range(rng.randint(3, 100))))
    for value in range(1, 101):
        arrays.add((value, -value, value + 1, -value - 1, value + 2, -value - 2))
    return [f"candidate(arr={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(arr=[0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])",
    "candidate(arr=[0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])",
    "candidate(arr=[3, 3, 6, 5, -2, 2, 5, 1, -9, 4])",
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
