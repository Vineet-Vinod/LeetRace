import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        candies = [1 + rng.randrange(10**7) for _ in range(1 + rng.randrange(80))]
        total = sum(candies)
        k = 1 + rng.randrange(total)
        calls.add(f"candidate(candies={candies!r}, k={k})")
    for case in range(300):
        candies = [1 + rng.randrange(10**7) for _ in range(1 + rng.randrange(80))]
        k = sum(candies) + 1 + rng.randrange(10**6)
        calls.add(f"candidate(candies={candies!r}, k={k})")
    calls.add(f"candidate(candies={[10**7] * 100_000!r}, k=1)")
    calls.add(f"candidate(candies={[1] * 100_000!r}, k=100_001)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(candies=[2, 5], k=11)",
    "candidate(candies=[5, 8, 6], k=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
