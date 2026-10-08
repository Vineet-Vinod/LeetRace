import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        total = rng.randint(1, 10**6)
        cost1, cost2 = rng.randint(1, 10**6), rng.randint(1, 10**6)
        calls.add(f"candidate(total={total}, cost1={cost1}, cost2={cost2})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(total=20, cost1=10, cost2=5)",
    "candidate(total=5, cost1=10, cost2=10)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
