import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        possible = [rng.randint(0, 1) for _ in range(rng.randint(2, 1000))]
        calls.add(f"candidate(possible={possible!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(possible=[0, 0])",
    "candidate(possible=[1, 0, 1, 0])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
