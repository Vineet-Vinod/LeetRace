import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = [1234, 65875, 247, 1]
    seen = set(vals)
    while len(vals) < 600:
        n = r.randint(1, 10**9)
        if n not in seen:
            seen.add(n)
            vals.append(n)
    return [f"candidate(num={n})" for n in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = ["candidate(num=1000000000)"]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
