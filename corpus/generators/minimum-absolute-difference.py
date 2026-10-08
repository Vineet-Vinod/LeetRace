def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (-1, 3, 4, 8, 10),
        (4, 2, 1, 3),
        (1, 1, 1),
        (0, 0) + tuple(range(2, 100000)),
    }
    while len(arrays) < 600:
        arrays.add(
            tuple(rng.randint(-1000000, 1000000) for _ in range(rng.randint(2, 100)))
        )
    return [f"candidate(arr={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(arr=[4, 2, 1, 3])",
    "candidate(arr=[1, 3, 6, 10, 15])",
    "candidate(arr=[3, 8, -10, 23, 19, -4, -14, 27])",
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
