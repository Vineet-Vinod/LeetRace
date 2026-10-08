import random

_STATEMENT_EXAMPLES = (
    "candidate(arr=[1, 2, 3])",
    "candidate(arr=[1, 1, 3, 3, 5, 5, 7, 7])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays with values in [0,1000], including successor chains."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        size = 1000 if len(calls) == 0 else rng.randint(1, 100)
        arr = [rng.randint(0, 1000) for _ in range(size)]
        if len(calls) > 0 and rng.randrange(2):
            start = rng.randint(0, 990)
            arr.extend((start, start + 1))
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
