def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    intervals = {(1, 22), (47, 85), (1, 10000), (99, 101)}
    while len(intervals) < 600:
        left = rng.randint(1, 10000)
        right = rng.randint(left, min(10000, left + 200))
        intervals.add((left, right))
    return [f"candidate(left={a}, right={b})" for a, b in sorted(intervals)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(left=1, right=22)",
    "candidate(left=47, right=85)",
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
