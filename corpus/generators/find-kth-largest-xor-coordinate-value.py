import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        matrix = [[rng.randint(0, 10**6) for _ in range(cols)] for _ in range(rows)]
        k = rng.randint(1, rows * cols)
        calls.add(f"candidate(matrix={matrix!r}, k={k})")
    boundary = [[(row + col) % 2 for col in range(1000)] for row in range(1000)]
    calls.add(f"candidate(matrix={boundary!r}, k=500000)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(matrix=[[5, 2], [1, 6]], k=1)",
    "candidate(matrix=[[5, 2], [1, 6]], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = (
    "candidate(matrix=[[0] * 1000 for _ in range(1000)], k=1000000)",
    "candidate(matrix=[[1000000]], k=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
