def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (0,),
        (1,),
        (100,),
        (1, 2, 3),
        (1, 1, 1),
        (0, 1, 2, 3),
        tuple(i % 101 for i in range(100)),
    }
    while len(arrays) < 600:
        n = rng.randint(1, 100)
        arrays.add(tuple(rng.randint(0, 100) for _ in range(n)))
    return [f"candidate(batteryPercentages={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(batteryPercentages=[1, 1, 2, 1, 3])",
    "candidate(batteryPercentages=[0, 1, 2])",
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
