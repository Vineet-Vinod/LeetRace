import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    cases = [([3, 2, 2, 3], 3), ([0, 1, 2, 2, 3, 0, 4, 2], 2), ([], 1)]
    seen = set()
    while len(cases) < 600:
        a = [r.randint(0, 50) for _ in range(r.randint(0, 100))]
        v = r.randint(0, 50)
        key = (tuple(a), v)
        if key not in seen:
            seen.add(key)
            cases.append((a, v))
    return [f"candidate(nums={a!r}, val={v})" for a, v in cases]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(nums=[50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50], val=100)"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
