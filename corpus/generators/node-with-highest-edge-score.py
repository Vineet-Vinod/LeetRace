import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(2, 1000)
        edges = [rng.choice([x for x in range(n) if x != i]) for i in range(n)]
        calls.add(f"candidate(edges={edges!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(edges=[1, 0, 0, 0, 0, 7, 7, 5])",
    "candidate(edges=[2, 0, 0, 2])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
