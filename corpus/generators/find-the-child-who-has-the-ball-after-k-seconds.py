import random

_STATEMENT_EXAMPLES = (
    "candidate(n=3, k=5)",
    "candidate(n=5, k=6)",
    "candidate(n=4, k=2)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct inputs with 2..50 children and 1..50 seconds."""
    rng = random.Random(seed)
    pairs = {(2, 1), (2, 50), (50, 1), (50, 50)}
    while len(pairs) < 600:
        pairs.add((rng.randint(2, 50), rng.randint(1, 50)))
    return [f"candidate(n={n}, k={k})" for n, k in sorted(pairs)]


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
