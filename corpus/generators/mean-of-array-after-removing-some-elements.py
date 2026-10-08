def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        tuple(range(1, 21)),
        tuple([1] * 20),
        tuple(range(100, 120)),
        tuple(i % 100001 for i in range(1000)),
    }
    while len(arrays) < 600:
        n = rng.randint(1, 50) * 20
        arrays.add(tuple(rng.randint(0, 100000) for _ in range(n)))
    return [f"candidate(arr={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(arr=[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3])",
    "candidate(arr=[6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0])",
    "candidate(arr=[6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4])",
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
