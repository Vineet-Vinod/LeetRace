import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[8, 6, 1, 5, 3])",
    "candidate(nums=[5, 4, 8, 7, 10, 2])",
    "candidate(nums=[6, 5, 4, 3, 4, 5])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of length 3..50 with values in [1,50]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(1, 50) for _ in range(rng.randint(3, 50))]
        call = f"candidate(nums={nums!r})"
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
