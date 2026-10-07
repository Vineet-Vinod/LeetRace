import random

_STATEMENT_EXAMPLES = (
    "candidate(mat=[[1, 2], [3, 4]], r=1, c=4)",
    "candidate(mat=[[1, 2], [3, 4]], r=2, c=4)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty rectangular matrices and valid positive target dimensions."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        rows, cols = (
            (100, 100) if len(calls) == 0 else (rng.randint(1, 20), rng.randint(1, 20))
        )
        mat = [[rng.randint(-1000, 1000) for _ in range(cols)] for _ in range(rows)]
        if rng.randrange(2):
            r, c = rows, cols
        else:
            r = rng.randint(1, 30)
            c = rng.randint(1, 30)
        call = f"candidate(mat={mat!r}, r={r}, c={c})"
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
