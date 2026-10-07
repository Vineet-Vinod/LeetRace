import random

_STATEMENT_EXAMPLES = ("candidate(n=22)", "candidate(n=8)", "candidate(n=5)")


def generate(seed: int = 0) -> list[str]:
    """Sample 600 distinct integers in the stated range [1, 10^9]."""
    rng = random.Random(seed)
    values = {1, 5, 6, 8, 22, 1_000_000_000}
    while len(values) < 600:
        values.add(rng.randint(1, 1_000_000_000))
    return [f"candidate(n={value})" for value in sorted(values)]


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
