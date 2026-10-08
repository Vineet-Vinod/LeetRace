import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(0, 100000) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[0])",
    "candidate(nums=[2, 5, 3, 9, 5, 3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
