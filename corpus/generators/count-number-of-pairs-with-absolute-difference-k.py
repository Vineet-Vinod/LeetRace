import random

_STATEMENT_EXAMPLES = (
    "candidate(nums=[1, 2, 2, 1], k=1)",
    "candidate(nums=[1, 3], k=3)",
    "candidate(nums=[3, 2, 1, 5, 4], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 1..200 values in [1,100] and k in [1,99], including bounds."""
    rng = random.Random(seed)
    calls = [
        "candidate(nums=[1], k=1)",
        "candidate(nums=[100, 100], k=99)",
        f"candidate(nums={list(range(1, 101))!r}, k=1)",
        f"candidate(nums={list(range(1, 101))!r}, k=99)",
    ]
    seen = set(calls)
    while len(calls) < 600:
        nums = [rng.randint(1, 100) for _ in range(rng.randint(1, 200))]
        k = rng.randint(1, 99)
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
