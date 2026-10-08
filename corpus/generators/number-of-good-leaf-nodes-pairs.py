import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 40)
        values = [rng.randint(1, 100) for _ in range(n)]
        for i in range(1, n):
            if values[(i - 1) // 2] is None:
                values[i] = None
        while values and values[-1] is None:
            values.pop()
        distance = rng.randint(1, 10)
        calls.add(f"candidate(tree_node({values!r}), distance={distance})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([1, 2, 3, 4, 5, 6, 7]), distance=3)",
    "candidate(root=tree_node([1, 2, 3, None, 4]), distance=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
