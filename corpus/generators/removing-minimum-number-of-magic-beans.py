import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        beans = [rng.randint(1, 100000) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(beans={beans!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(beans=[2, 10, 3, 2])",
    "candidate(beans=[4, 1, 6, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
