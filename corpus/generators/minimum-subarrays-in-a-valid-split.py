import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.update(
        (
            "candidate(nums=" + repr([2] * 1000) + ")",
            "candidate(nums=" + repr([2, 3] * 500) + ")",
        )
    )
    while len(calls) < 600:
        nums = [rng.randint(1, 100000) for _ in range(rng.randint(1, 100))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 1])",
    "candidate(nums=[2, 6, 3, 4, 3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
