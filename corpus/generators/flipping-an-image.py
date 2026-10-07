def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {tuple(tuple(0 for _ in range(20)) for _ in range(20))}
    while len(cases) < 600:
        n = rng.randint(1, 20)
        cases.add(tuple(tuple(rng.randrange(2) for _ in range(n)) for _ in range(n)))
    return [f"candidate(image={list(map(list, a))!r})" for a in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]])",
    "candidate(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])",
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
