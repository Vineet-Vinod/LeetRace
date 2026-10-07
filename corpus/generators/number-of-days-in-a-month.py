import random

_STATEMENT_EXAMPLES = (
    "candidate(year=1992, month=7)",
    "candidate(year=2000, month=2)",
    "candidate(year=1900, month=2)",
)


def generate(seed: int = 0) -> list[str]:
    """Sample 600 distinct valid year/month pairs from 1583..2100 and 1..12."""
    rng = random.Random(seed)
    pairs = {(1583, 1), (2000, 2), (1900, 2), (2100, 12)}
    while len(pairs) < 600:
        pairs.add((rng.randint(1583, 2100), rng.randint(1, 12)))
    return [f"candidate(year={year}, month={month})" for year, month in sorted(pairs)]


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
