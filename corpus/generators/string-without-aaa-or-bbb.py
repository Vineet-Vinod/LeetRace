import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        a, b = rng.randint(0, 100), rng.randint(0, 100)
        if max(a, b) <= 2 * (min(a, b) + 1):
            calls.add(f"candidate(a={a}, b={b})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(a=1, b=2)",
    "candidate(a=4, b=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = (
    "candidate(a=0, b=0)",
    "candidate(a=0, b=2)",
    "candidate(a=49, b=100)",
    "candidate(a=100, b=100)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
