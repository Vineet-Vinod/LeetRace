import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = [(5, 2), (3, 3), (1, 1)]
    seen = set(vals)
    while len(vals) < 600:
        pair = (r.randint(1, 50), r.randint(1, 50))
        if pair not in seen:
            seen.add(pair)
            vals.append(pair)
    return [f"candidate(n={n}, limit={child_limit})" for n, child_limit in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = ["candidate(n=50, limit=50)"]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
