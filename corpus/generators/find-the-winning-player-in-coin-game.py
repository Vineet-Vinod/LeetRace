def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {(2, 7), (4, 11), (1, 10), (10, 40), (100, 100)}
    while len(cases) < 600:
        cases.add((rng.randint(1, 100), rng.randint(1, 100)))
    return [f"candidate(x={x}, y={y})" for x, y in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = ["candidate(x=2, y=7)", "candidate(x=4, y=11)"]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
