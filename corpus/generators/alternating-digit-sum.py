def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 9, 10, 11, 99, 100, 101, 521, 886996, 10**9}
    while len(values) < 600:
        digits = rng.randint(1, 10)
        values.add(rng.randint(10 ** (digits - 1), min(10**9, 10**digits - 1)))
    return [f"candidate(n={n})" for n in sorted(values)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(n=521)",
    "candidate(n=111)",
    "candidate(n=886996)",
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
