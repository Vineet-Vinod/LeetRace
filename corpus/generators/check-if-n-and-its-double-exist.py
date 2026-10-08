import random

_STATEMENT_EXAMPLES = ("candidate(arr=[10, 2, 5, 3])", "candidate(arr=[3, 1, 7, 11])")


def generate(seed: int = 0) -> list[str]:
    """Generate distinct arrays of length 2..500 with values in [-1000,1000]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        n = 500 if len(calls) == 0 else rng.randint(2, 40)
        arr = [rng.randint(-1000, 1000) for _ in range(n)]
        call = f"candidate(arr={arr!r})"
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
