def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    arrays = {
        (4, 1, 4, 0, 3, 5),
        (1, 100),
        (1, 2, 3, 4),
        tuple(i % 101 for i in range(100)),
        tuple([0, 100] * 50),
        tuple(range(100)),
    }
    while len(arrays) < 600:
        n = 2 * rng.randint(1, 50)
        arrays.add(tuple(rng.randint(0, 100) for _ in range(n)))
    for nums in arrays:
        assert 2 <= len(nums) <= 100 and len(nums) % 2 == 0
        assert all(0 <= value <= 100 for value in nums)
    return [f"candidate(nums={list(a)!r})" for a in sorted(arrays)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(nums=[4, 1, 4, 0, 3, 5])",
    "candidate(nums=[1, 100])",
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
