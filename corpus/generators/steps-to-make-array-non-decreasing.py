import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[4, 5, 7, 7, 13])",
    "candidate(nums=[5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
