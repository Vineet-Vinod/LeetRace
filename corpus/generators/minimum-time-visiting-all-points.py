def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((1, 1), (3, 4), (-1, 0)),
        ((3, 2), (-2, 2)),
        tuple((i, -i) for i in range(100)),
    }
    while len(cases) < 600:
        points = tuple(
            (rng.randint(-1000, 1000), rng.randint(-1000, 1000))
            for _ in range(rng.randint(1, 50))
        )
        cases.add(points)
    return [f"candidate(points={list(map(list, p))!r})" for p in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(points=[[1, 1], [3, 4], [-1, 0]])",
    "candidate(points=[[3, 2], [-2, 2]])",
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
