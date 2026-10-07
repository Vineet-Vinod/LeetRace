import random

_STATEMENT_EXAMPLES = (
    "candidate(cost=[10, 15, 20])",
    "candidate(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate cost arrays of length 2..1000 with costs in [0,999]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        n = 1000 if len(calls) == 0 else rng.randint(2, 100)
        cost = [rng.randint(0, 999) for _ in range(n)]
        call = f"candidate(cost={cost!r})"
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
