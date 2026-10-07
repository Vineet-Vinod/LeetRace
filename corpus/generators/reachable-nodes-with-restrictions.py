import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(2, 100)
        edges = [[node, rng.randrange(node)] for node in range(1, n)]
        restricted = rng.sample(range(1, n), rng.randint(1, n - 1))
        calls.add(f"candidate(n={n}, edges={edges!r}, restricted={restricted!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=7, edges=[[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], restricted=[4, 2, 1])",
    "candidate(n=7, edges=[[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted=[4, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
