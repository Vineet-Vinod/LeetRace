def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {(1, 2), (1, 2, 3), (1, 1), (1, 2, 3, 2, 4), tuple(range(1, 1001))}
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(1, 1000) for _ in range(rng.randint(2, 1000))))
    for duplicate in range(1, 100):
        arrays.add(tuple(range(1, duplicate + 1)) + (duplicate,))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[1, 2, 10, 5, 7])",
    "candidate(nums=[2, 3, 1, 2])",
    "candidate(nums=[1, 1, 1])",
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
