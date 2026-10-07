import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        rows, cols = rng.randint(1, 30), rng.randint(1, 30)
        land = [[0] * cols for _ in range(rows)]
        for _ in range(rng.randint(0, 20)):
            top = rng.randrange(rows)
            left = rng.randrange(cols)
            bottom = min(rows - 1, top + rng.randint(0, 2))
            right = min(cols - 1, left + rng.randint(0, 2))
            if all(
                land[r][c] == 0
                for r in range(max(0, top - 1), min(rows, bottom + 2))
                for c in range(max(0, left - 1), min(cols, right + 2))
            ):
                for r in range(top, bottom + 1):
                    for c in range(left, right + 1):
                        land[r][c] = 1
        calls.add(f"candidate(land={land!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(land=[[0]])",
    "candidate(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
