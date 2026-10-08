def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((4, 1, 2), (1, 3, 4, 2)),
        ((2, 4), (1, 2, 3, 4)),
        (tuple(range(0, 1000, 2)), tuple(range(1000))),
    }
    while len(cases) < 600:
        n = rng.randint(1, 50)
        b = tuple(rng.sample(range(0, 10001), n))
        a = tuple(rng.sample(b, rng.randint(1, n)))
        cases.add((a, b))
    return [
        f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])",
    "candidate(nums1=[2, 4], nums2=[1, 2, 3, 4])",
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
