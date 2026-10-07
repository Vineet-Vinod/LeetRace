import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = ["B0B6G0R6R0R6G9", "B0R0G0R9R0B0"]
    seen = set(vals)
    while len(vals) < 600:
        s = "".join(
            r.choice("RGB") + str(r.randrange(10)) for _ in range(r.randint(1, 30))
        )
        if s not in seen:
            seen.add(s)
            vals.append(s)
    return [f"candidate(rings={s!r})" for s in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(rings='R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0G0B0R0')"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_EXAMPLE_CALLS = ["candidate(rings='B0R0G0R9R0B0G0')", "candidate(rings='G4')"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
