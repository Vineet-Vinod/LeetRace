import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[1, 3, 7, 15])",
    "candidate(nums=[8, 4, 2])",
    "candidate(nums=[5, 4, 9, 11])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct arrays of length 2..100 with values in [0,100]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        n = 100 if len(calls) == 0 else rng.randint(2, 100)
        nums = [100] * n if len(calls) == 0 else [rng.randint(0, 100) for _ in range(n)]
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
