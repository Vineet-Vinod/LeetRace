def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (1000, 2000, 3000),
        (4000, 3000, 2000, 1000),
        (1000, 1001, 1002),
        tuple(rng.sample(range(1000, 1000001), 100)),
    }
    while len(arrays) < 600:
        n = rng.randint(3, 20)
        arrays.add(tuple(sorted(rng.sample(range(1000, 1000001), n))))
    return [f"candidate(salary={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(salary=[4000, 3000, 1000, 2000])",
    "candidate(salary=[1000, 2000, 3000])",
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
