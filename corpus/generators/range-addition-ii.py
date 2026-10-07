def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        (3, 3, ((2, 2), (3, 3))),
        (3, 3, ()),
        (1, 1, ((1, 1),)),
        (40000, 40000, tuple((40000, 40000) for _ in range(10000))),
    }
    while len(cases) < 600:
        m, n = rng.randint(1, 40000), rng.randint(1, 40000)
        ops = tuple(
            (rng.randint(1, m), rng.randint(1, n)) for _ in range(rng.randint(0, 100))
        )
        cases.add((m, n, ops))
    return [
        f"candidate(m={m}, n={n}, ops={list(map(list, o))!r})"
        for m, n, o in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(m=3, n=3, ops=[[2, 2], [3, 3]])",
    "candidate(m=3, n=3, ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])",
    "candidate(m=3, n=3, ops=[])",
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
