import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        rows, cols = 1 + rng.randrange(20), 1 + rng.randrange(20)
        values = sorted(rng.sample(range(-10000, 10001), rows * cols))
        matrix = [values[row * cols : (row + 1) * cols] for row in range(rows)]
        target = rng.choice(values)
        calls.add(f"candidate(matrix={matrix!r}, target={target})")
    for case in range(300):
        rows, cols = 1 + rng.randrange(20), 1 + rng.randrange(20)
        values = sorted(rng.sample(range(-10000, 10001), rows * cols))
        matrix = [values[row * cols : (row + 1) * cols] for row in range(rows)]
        missing = sorted(set(range(-10000, 10001)) - set(values))
        target = rng.choice(missing)
        calls.add(f"candidate(matrix={matrix!r}, target={target})")
    values = list(range(-5000, 5000))
    matrix = [values[row * 100 : (row + 1) * 100] for row in range(100)]
    calls.add(f"candidate(matrix={matrix!r}, target=-10000)")
    calls.add(f"candidate(matrix={matrix!r}, target=4999)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)",
    "candidate(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = (
    "candidate(matrix=[[-10000, 10000]], target=-10000)",
    "candidate(matrix=[[-10000, 10000]], target=10000)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
