import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 1000)
        k = rng.randint(1, n)
        nums = [rng.randint(1, 100000) for _ in range(n)]
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 1, 1, 1, 2, 3, 4], k=4)",
    "candidate(nums=[1, 2, 3, 2, 2, 1, 3], k=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
