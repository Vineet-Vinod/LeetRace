import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(2, 100)
        roads = [
            [a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.05
        ]
        if not roads:
            roads = [[0, 1]]
        calls.add(f"candidate(n={n}, roads={roads!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])",
    "candidate(n=5, roads=[[0, 3], [2, 4], [1, 3]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
