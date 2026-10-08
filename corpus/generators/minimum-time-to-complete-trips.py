import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        time = [rng.randint(1, 10**7) for _ in range(rng.randint(1, 1000))]
        total = rng.randint(1, 10**7)
        calls.add(f"candidate(time={time!r}, totalTrips={total})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(time=[1, 2, 3], totalTrips=5)",
    "candidate(time=[2], totalTrips=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
