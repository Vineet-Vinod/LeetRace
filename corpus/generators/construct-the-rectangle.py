import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    rng = random.Random(seed)
    vals = [1, 2, 3, 4, 37, 10000000]
    seen = set(vals)
    while len(vals) < 600:
        n = rng.randint(1, 10000000)
        if n not in seen:
            seen.add(n)
            vals.append(n)
    return [f"candidate(area={n})" for n in vals]


_EXAMPLE_CALLS = ["candidate(area=122122)"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
