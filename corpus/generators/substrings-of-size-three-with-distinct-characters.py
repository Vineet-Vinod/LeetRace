import random
import string

_STATEMENT_EXAMPLES = ("candidate(s='xyzzaz')", "candidate(s='aababcabc')")


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings of length 1..100, including shorter-than-window cases."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
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
