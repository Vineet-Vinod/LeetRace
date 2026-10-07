import random


def generate(seed: int = 0) -> list[str]:
    """Strings have length 1 through 20 and contain only ASCII letters, digits, or allowed test punctuation."""
    r = random.Random(seed)
    vals = ["234Adas", "b3", "a3$e", "UuE"]
    seen = set(vals)
    while len(vals) < 600:
        s = "".join(
            r.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$"
            )
            for _ in range(r.randint(1, 20))
        )
        if s not in seen:
            seen.add(s)
            vals.append(s)
    return [f"candidate(word={s!r})" for s in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = ["candidate(word='aaaaaaaaaaaaaaaaaaaB')"]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]
