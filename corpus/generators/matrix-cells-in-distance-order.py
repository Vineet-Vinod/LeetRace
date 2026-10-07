import random

_STATEMENT_EXAMPLES = (
    "candidate(rows=1, cols=2, rCenter=0, cCenter=0)",
    "candidate(rows=2, cols=2, rCenter=0, cCenter=1)",
    "candidate(rows=2, cols=3, rCenter=1, cCenter=2)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct grids with valid centers; only a few grids are large."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        if len(calls) == 0:
            rows, cols = 1, 1
        elif len(calls) == 1:
            rows, cols = 100, 100
        else:
            rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        r, c = rng.randrange(rows), rng.randrange(cols)
        call = f"candidate(rows={rows}, cols={cols}, rCenter={r}, cCenter={c})"
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
