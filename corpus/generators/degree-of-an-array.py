import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[1, 2, 2, 3, 1])",
    "candidate(nums=[1, 2, 2, 3, 1, 4, 2])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of length 1..50000 with values in [0,49999]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        n = 50_000 if len(calls) == 0 else rng.randint(1, 100)
        nums = [rng.randint(0, 49999) for _ in range(n)]
        if nums and len(calls) > 0 and rng.randrange(2):
            nums.extend([nums[0]] * rng.randint(1, 5))
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
