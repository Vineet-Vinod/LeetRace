import random


def generate(seed: int = 0) -> list[str]:
    """Every n is within 0 through 100,000; routine cases remain modest and one boundary case is included."""
    r = random.Random(seed)
    vals = [0, 1, 2, 5, 31, 32, 10000]
    seen = set(vals)
    while len(vals) < 600:
        n = r.randint(0, 700)
        if n not in seen:
            seen.add(n)
            vals.append(n)
    return [f"candidate(n={n})" for n in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = ["candidate(n=100000)"]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
