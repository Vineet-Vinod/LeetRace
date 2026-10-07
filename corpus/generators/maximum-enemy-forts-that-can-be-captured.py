def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (1, 0, 0, -1),
        (0, 0, 1, -1),
        (1, 0, 0, 0, 0, 1),
        (1,) + (0,) * 998 + (-1,),
    }
    while len(arrays) < 600:
        arrays.add(
            tuple(rng.choice((-1, 0, 0, 0, 1)) for _ in range(rng.randint(1, 100)))
        )
    return [f"candidate(forts={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(forts=[1, 0, 0, -1, 0, 0, 0, 0, 1])",
    "candidate(forts=[0, 0, 1, -1])",
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
