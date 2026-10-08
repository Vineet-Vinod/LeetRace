def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {(1,), (1, 2), (1, 2, 3), (1, 1, 3, 3), (-3, -2, -1, 0, 1)}
    while len(arrays) < 600:
        n = rng.randint(1, 100)
        arrays.add(tuple(rng.randint(-100, 100) for _ in range(n)))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[11, 7, 2, 15])",
    "candidate(nums=[-3, 3, 3, 90])",
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
