import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        prices = [rng.randint(1, 100000) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(prices={prices!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(prices=[3, 2, 1, 4])",
    "candidate(prices=[8, 6, 7, 7])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
