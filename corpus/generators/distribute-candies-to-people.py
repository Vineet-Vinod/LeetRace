import random

_STATEMENT_EXAMPLES = (
    "candidate(candies=7, num_people=4)",
    "candidate(candies=10, num_people=3)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate candies in [1,10^9] and recipient counts in [1,1000]."""
    rng = random.Random(seed)
    pairs = {(1, 1), (10, 3), (10**9, 1000)}
    while len(pairs) < 600:
        pairs.add((rng.randint(1, 1000), rng.randint(1, 1000)))
    return [f"candidate(candies={a}, num_people={b})" for a, b in sorted(pairs)]


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
