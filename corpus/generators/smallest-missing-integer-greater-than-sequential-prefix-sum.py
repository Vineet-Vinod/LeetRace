import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[1, 2, 3, 2, 5])",
    "candidate(nums=[3, 4, 5, 1, 12, 14, 13])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays of 1..50 values, each value in [1,50]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(1, 50) for _ in range(rng.randint(1, 50))]
        if rng.randrange(2) and len(nums) < 50:
            start = rng.randint(1, 30)
            nums[:0] = list(range(start, min(start + rng.randint(1, 10), 51)))
            nums = nums[:50]
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
