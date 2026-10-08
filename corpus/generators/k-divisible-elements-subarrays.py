import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 40)
        nums = [rng.randint(1, 200) for _ in range(n)]
        k = rng.randint(1, n)
        p = rng.randint(1, 200)
        calls.add(f"candidate(nums={nums!r}, k={k}, p={p})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 4], k=4, p=1)",
    "candidate(nums=[2, 3, 3, 2, 2], k=2, p=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
