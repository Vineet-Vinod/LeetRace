import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[7, 12, 9, 8, 9, 15], k=4)",
    "candidate(nums=[2, 12, 1, 11, 4, 5], k=6)",
    "candidate(nums=[10, 8, 5, 9, 11, 6, 8], k=1)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of 1..50 values in [0, 2^31-1], including bit-30 bounds."""
    rng = random.Random(seed)
    calls = [
        "candidate(nums=[0], k=1)",
        f"candidate(nums={[2**30]!r}, k=1)",
        f"candidate(nums={[2**31 - 1]!r}, k=1)",
        f"candidate(nums={[2**30, 2**30, 0]!r}, k=2)",
        f"candidate(nums={[2**31 - 1] * 50!r}, k=50)",
    ]
    seen = set(calls)
    while len(calls) < 600:
        nums = [rng.randint(0, 2**31 - 1) for _ in range(rng.randint(1, 50))]
        k = rng.randint(1, len(nums))
        call = f"candidate(nums={nums!r}, k={k})"
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
