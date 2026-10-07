import random

_STATEMENT_EXAMPLES = (
    "candidate(num=[1, 2, 0, 0], k=34)",
    "candidate(num=[2, 7, 4], k=181)",
    "candidate(num=[2, 1, 5], k=806)",
)


def generate(seed: int = 0) -> list[str]:
    """Build 600 distinct valid digit arrays and nonnegative addends."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    for index in range(600):
        if index == 0:
            num, k = [0], 1
        elif index == 1:
            num, k = [9] * 10_000, 10_000
        else:
            length = rng.randint(1, 100)
            num = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(length - 1)]
            k = rng.randint(1, 10_000)
        call = f"candidate(num={num!r}, k={k})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    while len(calls) < 600:
        num = [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(99)]
        k = rng.randint(1, 10_000)
        call = f"candidate(num={num!r}, k={k})"
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
