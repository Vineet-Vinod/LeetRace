def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {(1, 2, 3, 2), (1, 1, 1, 1, 1), (1, 2, 3, 4, 5)}
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[1, 2, 3, 2])",
    "candidate(nums=[1, 1, 1, 1, 1])",
    "candidate(nums=[1, 2, 3, 4, 5])",
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
