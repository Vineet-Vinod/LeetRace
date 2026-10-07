import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {
        "candidate(n=65535, cost=[1] * 65535)",
        "candidate(n=32767, cost=[10000] * 32767)",
    }
    while len(calls) < 600:
        levels = rng.randint(2, 9)
        n = (1 << levels) - 1
        cost = [rng.randint(1, 10000) for _ in range(n)]
        calls.add(f"candidate(n={n}, cost={cost!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=3, cost=[5, 3, 3])",
    "candidate(n=7, cost=[1, 5, 2, 2, 3, 3, 1])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
