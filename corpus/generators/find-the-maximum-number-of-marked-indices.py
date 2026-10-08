import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[3, 5, 2, 4])",
    "candidate(nums=[9, 2, 5, 4])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
