def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((5, 3, 6, 1, 12), 3),
        ((2, 7, 9), 4),
        ((1,), 1),
        (tuple(range(1, 1001)), 1000),
    }
    while len(cases) < 600:
        original = rng.randint(1, 1000)
        nums = tuple(rng.sample(range(1, 1001), rng.randint(1, 50)))
        cases.add((nums, original))
    return [f"candidate(nums={list(a)!r}, original={b})" for a, b in sorted(cases)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[5, 3, 6, 1, 12], original=3)",
    "candidate(nums=[2, 7, 9], original=4)",
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
