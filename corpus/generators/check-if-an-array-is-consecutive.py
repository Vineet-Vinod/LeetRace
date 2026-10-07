def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (1,),
        (1, 2),
        (2, 1),
        (1, 2, 3),
        (1, 1, 2),
        (0, 1, 2),
        tuple(range(100000)),
    }
    while len(arrays) < 600:
        n = rng.randint(1, 50)
        arrays.add(tuple(rng.randint(0, 100000) for _ in range(n)))
    for start in range(100):
        n = start % 50 + 1
        arrays.add(tuple(rng.sample(range(start * 1000, start * 1000 + n), n)))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[1, 3, 4, 2])",
    "candidate(nums=[1, 3])",
    "candidate(nums=[3, 5, 4])",
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
