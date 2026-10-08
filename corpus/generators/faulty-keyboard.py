import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = ["string", "poiinter", "abc", "aiii"]
    seen = set(vals)
    while len(vals) < 600:
        s = r.choice("abcde") + "".join(
            r.choice("abcdeixyz") for _ in range(r.randint(0, 99))
        )
        if s not in seen:
            seen.add(s)
            vals.append(s)
    return [f"candidate(s={s!r})" for s in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(s='aiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
