import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 1000)
        k = rng.randint(1, (n + 1) // 2)
        nums = [rng.randint(1, 10**9) for _ in range(n)]
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[2, 3, 5, 9], k=2)",
    "candidate(nums=[2, 7, 9, 3, 1], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
