def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((1, 2, 3), (2, 4, 6)),
        ((1, 2, 3, 3), (1, 1, 2, 2)),
        (tuple(range(-1000, 0)), tuple(range(0, 1000))),
    }
    while len(cases) < 600:
        cases.add(
            (
                tuple(rng.randint(-100, 100) for _ in range(rng.randint(1, 100))),
                tuple(rng.randint(-100, 100) for _ in range(rng.randint(1, 100))),
            )
        )
    return [
        f"candidate(nums1={list(a)!r}, nums2={list(b)!r})" for a, b in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums1=[1, 2, 3], nums2=[2, 4, 6])",
    "candidate(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2])",
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
