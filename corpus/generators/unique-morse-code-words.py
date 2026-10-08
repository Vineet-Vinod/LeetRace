import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    cases = [["gin", "zen", "gig", "msg"], ["a"]]
    seen = {tuple(x) for x in cases}
    while len(cases) < 600:
        a = [
            "".join(
                r.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(r.randint(1, 12))
            )
            for _ in range(r.randint(1, 30))
        ]
        key = tuple(a)
        if key not in seen:
            seen.add(key)
            cases.append(a)
    return [f"candidate(words={a!r})" for a in cases]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(words=['aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaa'])"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
