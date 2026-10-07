import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        n = 1 + rng.randrange(100)
        first, second = rng.sample(range(n), min(2, n)) if n > 1 else (0, 0)
        fruits = [rng.choice((first, second)) for _ in range(n)]
        calls.add(f"candidate(fruits={fruits!r})")
    for case in range(300):
        n = 3 + rng.randrange(100)
        fruits = [rng.randrange(n) for _ in range(n)]
        calls.add(f"candidate(fruits={fruits!r})")
    calls.add(f"candidate(fruits={list(range(100_000))!r})")
    calls.add(f"candidate(fruits={[0, 1] * 50_000!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(fruits=[1, 2, 1])",
    "candidate(fruits=[1, 2, 3, 2, 2])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
