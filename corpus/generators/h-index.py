import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        citations = [rng.randint(0, 1000) for _ in range(rng.randint(1, 5000))]
        calls.add(f"candidate(citations={citations!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(citations=[1, 3, 1])",
    "candidate(citations=[3, 0, 6, 1, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
