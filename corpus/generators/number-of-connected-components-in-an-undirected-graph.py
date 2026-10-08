import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 100)
        edges = [
            [a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.08
        ]
        calls.add(f"candidate(n={n}, edges={edges!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]])",
    "candidate(n=5, edges=[[0, 1], [1, 2], [3, 4]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
