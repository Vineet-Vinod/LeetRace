import random


def generate(seed: int = 0) -> list[str]:
    """All generated arguments stay within the statement bounds and follow the problem guarantees."""
    r = random.Random(seed)
    vals = ["I speak Goat Latin", "The quick brown fox"]
    seen = set(vals)
    while len(vals) < 600:
        sentence = " ".join(
            "".join(
                r.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                for _ in range(r.randint(1, 8))
            )
            for _ in range(r.randint(1, 12))
        )
        if sentence not in seen:
            seen.add(sentence)
            vals.append(sentence)
    return [f"candidate(sentence={s!r})" for s in vals]


_BASE_GENERATE = generate
_BOUNDARY_CALLS = [
    "candidate(sentence='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')"
]


def generate(seed: int = 0) -> list[str]:
    calls = _BASE_GENERATE(seed)
    return calls + [call for call in _BOUNDARY_CALLS if call not in calls]


_EXAMPLE_CALLS = ["candidate(sentence='The quick brown fox jumped over the lazy dog')"]

_PREVIOUS_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = _PREVIOUS_GENERATE(seed)
    return calls + [call for call in _EXAMPLE_CALLS if call not in calls]
