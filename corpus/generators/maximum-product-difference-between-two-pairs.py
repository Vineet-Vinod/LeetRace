def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (5, 6, 2, 7, 4),
        (4, 2, 5, 9, 7, 4, 8),
        (1, 1, 1, 1),
        tuple(range(1, 10001)),
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(1, 10000) for _ in range(rng.randint(4, 100))))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[5, 6, 2, 7, 4])",
    "candidate(nums=[4, 2, 5, 9, 7, 4, 8])",
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
