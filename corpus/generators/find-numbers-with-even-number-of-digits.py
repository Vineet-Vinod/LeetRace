def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (1,),
        (10,),
        (1, 2, 3, 4),
        (12, 345, 2, 6, 7896),
        (100000, 99999),
        tuple(range(1, 101)),
    }
    while len(arrays) < 600:
        arrays.add(tuple(rng.randint(1, 100000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[12, 345, 2, 6, 7896])",
    "candidate(nums=[555, 901, 482, 1771])",
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
