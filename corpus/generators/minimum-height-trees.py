import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 100)
        edges = [[node, rng.randrange(node)] for node in range(1, n)]
        rng.shuffle(edges)
        calls.add(f"candidate(n={n}, edges={edges!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=4, edges=[[1, 0], [1, 2], [1, 3]])",
    "candidate(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
