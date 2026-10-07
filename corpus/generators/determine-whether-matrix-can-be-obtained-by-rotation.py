def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        (
            (tuple(tuple(0 for _ in range(10)) for _ in range(10))),
            (tuple(tuple(0 for _ in range(10)) for _ in range(10))),
        )
    }
    while len(cases) < 600:
        n = rng.randint(1, 10)
        mat = tuple(tuple(rng.randrange(2) for _ in range(n)) for _ in range(n))
        target = [list(row) for row in mat]
        if rng.random() < 0.6:
            for _ in range(rng.randrange(4)):
                target = [list(row) for row in zip(*target[::-1])]
        else:
            target = [[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        cases.add((mat, tuple(tuple(row) for row in target)))
    return [
        f"candidate(mat={list(map(list, a))!r}, target={list(map(list, b))!r})"
        for a, b in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]])",
    "candidate(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]])",
    "candidate(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]])",
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
