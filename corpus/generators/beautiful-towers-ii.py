import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(maxHeights=[5, 3, 4, 1, 1])")
    while len(calls) < 600:
        size = rng.randint(1, 50)
        heights = [rng.randint(1, 10**9) for _ in range(size)]
        calls.add(f"candidate(maxHeights={heights!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(maxHeights=[3, 2, 5, 5, 2, 3])",
    "candidate(maxHeights=[6, 5, 3, 9, 2, 7])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
