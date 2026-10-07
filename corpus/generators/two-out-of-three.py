def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        ((1, 1, 3, 2), (2, 3), (3,)),
        (tuple(range(1, 101)), tuple(range(1, 101)), tuple(range(1, 101))),
    }
    while len(cases) < 600:
        rows = tuple(
            tuple(sorted(rng.sample(range(1, 101), rng.randint(1, 30))))
            for _ in range(3)
        )
        cases.add(rows)
    return [
        f"candidate(nums1={list(a)!r}, nums2={list(b)!r}, nums3={list(c)!r})"
        for a, b, c in sorted(cases)
    ]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums1=[1, 1, 3, 2], nums2=[2, 3], nums3=[3])",
    "candidate(nums1=[3, 1], nums2=[2, 3], nums3=[1, 2])",
    "candidate(nums1=[1, 2, 2], nums2=[4, 3, 3], nums3=[5])",
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
