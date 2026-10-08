def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 2, 3, 4, 7, 10, 19, 20, 100, 999999999, 10**9}
    while len(values) < 600:
        values.add(rng.randint(1, 10**9))
    return [f"candidate(n={n})" for n in sorted(values)]


_STATEMENT_EXAMPLE_CALLS = ["candidate(n=19)", "candidate(n=2)"]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
