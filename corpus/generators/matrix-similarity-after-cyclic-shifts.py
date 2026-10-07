def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        (((1,),), 1),
        (((1, 2, 3),), 1),
        (tuple(tuple(1 for _ in range(25)) for _ in range(25)), 50),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 25), rng.randint(1, 25)
        matrix = tuple(
            tuple(rng.randint(1, 25) for _ in range(cols)) for _ in range(rows)
        )
        cases.add((matrix, rng.randint(1, 50)))
    return [f"candidate(mat={list(map(list, m))!r}, k={k})" for m, k in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=4)",
    "candidate(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2)",
    "candidate(mat=[[2, 2], [2, 2]], k=3)",
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
