import random

_STATEMENT_EXAMPLES = ("candidate(left=6, right=10)", "candidate(left=10, right=15)")


def generate(seed: int = 0) -> list[str]:
    """Generate valid intervals with 1 <= left <= right <= 10^6 and width <= 10^4."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        left = rng.randint(1, 1_000_000)
        right = min(1_000_000, left + rng.randint(0, 10_000))
        call = f"candidate(left={left}, right={right})"
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
