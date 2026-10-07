import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 1000)
        points = []
        for _ in range(n):
            start = rng.randint(-(2**31), 2**31 - 2)
            end = rng.randint(start + 1, min(2**31 - 1, start + 10000))
            points.append([start, end])
        calls.add(f"candidate(points={points!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(points=[[1, 2], [2, 3], [3, 4], [4, 5]])",
    "candidate(points=[[10, 16], [2, 8], [1, 6], [7, 12]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
