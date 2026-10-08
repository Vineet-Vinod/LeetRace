def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {(0,), (0, 1), (1, 0), (4, 5, 0, 1, 2, 3), tuple(range(1000))}
    while len(arrays) < 600:
        n = rng.randint(1, 100)
        arrays.add(tuple(rng.sample(range(n), n)))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[0, 2, 1, 5, 3, 4])",
    "candidate(nums=[5, 0, 1, 2, 3, 4])",
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
