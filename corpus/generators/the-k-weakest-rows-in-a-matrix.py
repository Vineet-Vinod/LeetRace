import random

_STATEMENT_EXAMPLES = (
    "candidate(mat=[[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], k=3)",
    "candidate(mat=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 2..100 row/column matrices with sorted binary rows and valid k."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        rows, cols = (
            (100, 100) if len(calls) == 1 else (rng.randint(2, 20), rng.randint(2, 20))
        )
        mat = []
        for _ in range(rows):
            soldiers = rng.randint(0, cols)
            mat.append([1] * soldiers + [0] * (cols - soldiers))
        k = rng.randint(1, rows)
        call = f"candidate(mat={mat!r}, k={k})"
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
