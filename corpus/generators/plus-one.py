def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {(1,), (9,), (1, 2, 3), (9, 9, 9), (8, 9, 9), (9,) * 100}
    while len(arrays) < 600:
        n = rng.randint(1, 100)
        first = rng.randint(1, 9)
        arrays.add(tuple([first] + [rng.randint(0, 9) for _ in range(n - 1)]))
    return [f"candidate(digits={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(digits=[1, 2, 3])",
    "candidate(digits=[4, 3, 2, 1])",
    "candidate(digits=[9])",
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
