def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((1, 2, 3), (2, 3, 4), (2, 3, 5)),
        ((1, 2, 3), (4, 5, 6)),
        (tuple(range(1, 1001)),),
    }
    while len(cases) < 600:
        count = rng.randint(1, 8)
        rows = tuple(
            tuple(sorted(rng.sample(range(1, 30), rng.randint(1, 15))))
            for _ in range(count)
        )
        cases.add(rows)
    return [f"candidate(nums={list(map(list, rows))!r})" for rows in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])",
    "candidate(nums=[[1, 2, 3], [4, 5, 6]])",
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
