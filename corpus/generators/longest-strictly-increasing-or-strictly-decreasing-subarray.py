import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    cases = [[1, 4, 3, 3, 2], [3, 3, 3], [1], [50, 49, 48, 47]]
    seen = {tuple(x) for x in cases}
    while len(cases) < 600:
        a = [r.randint(1, 50) for _ in range(r.randint(1, 50))]
        key = tuple(a)
        if key not in seen:
            seen.add(key)
            cases.append(a)
    return [f"candidate(nums={a!r})" for a in cases]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_EXAMPLE_CALLS = ["candidate(nums=[3, 3, 3, 3])", "candidate(nums=[3, 2, 1])"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
