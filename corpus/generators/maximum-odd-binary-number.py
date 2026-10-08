import random

_STATEMENT_EXAMPLES = ("candidate(s='010')", "candidate(s='0101')")


def generate(seed: int = 0) -> list[str]:
    """Return distinct binary strings of length 1..100 with at least one '1'."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        length = rng.randint(1, 100)
        bits = [rng.choice("01") for _ in range(length)]
        bits[rng.randrange(length)] = "1"
        s = "".join(bits)
        call = f"candidate(s={s!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
