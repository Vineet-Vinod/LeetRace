import random

_STATEMENT_EXAMPLES = ("candidate(moves='UD')", "candidate(moves='LL')")


def generate(seed: int = 0) -> list[str]:
    """Construct balanced and unbalanced walks across varied directions and lengths."""
    rng = random.Random(seed)
    calls: list[str] = []
    for length in range(1, 301):
        vertical = "U" * length
        calls.append(f"candidate(moves={(vertical + 'D' * length)!r})")
    for length in range(1, 301):
        moves = "U" * length
        calls.append(f"candidate(moves={moves!r})")
    rng.shuffle(calls)
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
