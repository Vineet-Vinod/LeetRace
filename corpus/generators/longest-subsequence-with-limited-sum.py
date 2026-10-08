import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[4, 5, 2, 1], queries=[3, 10, 21])",
    "candidate(nums=[2, 3, 4, 5], queries=[1])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 1..1000 positive nums and queries, each in [1,10^6]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        size = 1000 if len(calls) == 0 else rng.randint(1, 1000)
        nums = [rng.randint(1, 1_000_000) for _ in range(size)]
        queries = [rng.randint(1, 1_000_000) for _ in range(size)]
        call = f"candidate(nums={nums!r}, queries={queries!r})"
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
