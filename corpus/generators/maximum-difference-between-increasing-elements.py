import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[7, 1, 5, 4])",
    "candidate(nums=[9, 4, 3, 2])",
    "candidate(nums=[1, 5, 2, 10])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of length 2..1000 with positive values <= 10^9."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        n = 1000 if len(calls) == 1 else rng.randint(2, 100)
        nums = [rng.randint(1, 10**9) for _ in range(n)]
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
