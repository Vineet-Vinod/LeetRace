import random

_STATEMENT_EXAMPLES = (
    "candidate(position=[1, 2, 3])",
    "candidate(position=[2, 2, 2, 3, 3])",
    "candidate(position=[1, 1000000000])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate positions of 1..100 chips with positions in [1,10^9]."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        position = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        call = f"candidate(position={position!r})"
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
