import random

_STATEMENT_EXAMPLES = (
    "candidate(time='2?:?0')",
    "candidate(time='0?:3?')",
    "candidate(time='1?:22')",
)


def generate(seed: int = 0) -> list[str]:
    """Mask digits in valid 24-hour times; every generated time includes a '?'."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        hour, minute = rng.randrange(24), rng.randrange(60)
        chars = list(f"{hour:02}:{minute:02}")
        slots = [0, 1, 3, 4]
        for slot in slots:
            if rng.randrange(2):
                chars[slot] = "?"
        chars[rng.choice(slots)] = "?"
        time = "".join(chars)
        call = f"candidate(time={time!r})"
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
