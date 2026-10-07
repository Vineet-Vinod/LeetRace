import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = [(240, 2), (430043, 2), (1, 1)]
    seen = set(vals)
    while len(vals) < 600:
        n = r.randint(1, 1000000000)
        k = r.randint(1, len(str(n)))
        p = (n, k)
        if p not in seen:
            seen.add(p)
            vals.append(p)
    return [f"candidate(num={n}, k={k})" for n, k in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = ["candidate(num=1000000000, k=10)"]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
