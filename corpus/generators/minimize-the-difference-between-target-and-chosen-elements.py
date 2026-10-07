import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        mat = [[rng.randint(1, 70) for _ in range(cols)] for _ in range(rows)]
        target = rng.randint(1, 800)
        calls.add(f"candidate(mat={mat!r}, target={target})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], target=13)",
    "candidate(mat=[[1], [2], [3]], target=100)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
