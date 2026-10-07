import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        num1 = rng.randint(1, 10**9)
        num2 = rng.randint(-(10**9), 10**9)
        calls.add(f"candidate(num1={num1}, num2={num2})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(num1=3, num2=-2)",
    "candidate(num1=5, num2=7)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
