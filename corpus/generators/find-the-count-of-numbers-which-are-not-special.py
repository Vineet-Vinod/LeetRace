import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        left = rng.randint(1, 10**9)
        right = min(10**9, left + rng.randint(0, 100000))
        calls.add(f"candidate(l={left}, r={right})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(l=4, r=16)",
    "candidate(l=5, r=7)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
