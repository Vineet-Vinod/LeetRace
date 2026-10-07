import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 50)
        values: list[int | None] = [rng.randint(-100, 100) for _ in range(n)]
        for j in range(1, n):
            if values[(j - 1) // 2] is None:
                values[j] = None
        while values and values[-1] is None:
            values.pop()
        limit = rng.randint(-100000, 100000)
        calls.add(f"candidate(tree_node({values!r}), limit={limit})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([1, 2, -3, -5, None, 4, None]), limit=-1)",
    "candidate(root=tree_node([1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]), limit=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
