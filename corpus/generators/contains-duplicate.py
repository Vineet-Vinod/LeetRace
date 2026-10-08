import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[1, 2, 3, 1])",
    "candidate(nums=[1, 2, 3, 4])",
    "candidate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct arrays of length 1..100000 with bounded integer values."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    for index in range(600):
        n = 100_000 if index == 0 else 1 + index % 40
        nums = [rng.randint(-1_000_000_000, 1_000_000_000) for _ in range(n)]
        if index % 2 == 0 and n > 1:
            nums[-1] = nums[0]
        call = f"candidate(nums={nums!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    while len(calls) < 600:
        nums = [
            rng.randint(-1_000_000_000, 1_000_000_000)
            for _ in range(rng.randint(1, 50))
        ]
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
