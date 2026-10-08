import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    cases = [[1, 2, -1, -1, -1], [1, -1, 2, -1]]
    seen = {tuple(x) for x in cases}
    while len(cases) < 600:
        a = [r.choice([-1, r.randint(1, 100)]) for _ in range(r.randint(1, 60))]
        key = tuple(a)
        if key not in seen:
            seen.add(key)
            cases.append(a)
    return [f"candidate(nums={a!r})" for a in cases]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(nums=[100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1, 100, -1])"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_EXAMPLE_CALLS = ["candidate(nums=[1, -1, 2, -1, -1])"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
