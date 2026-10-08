import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 80)
        values: list[int | None] = [rng.randint(0, 25) for _ in range(size)]
        for index in range(1, size):
            if values[(index - 1) // 2] is None:
                values[index] = None
        while values and values[-1] is None:
            values.pop()
        calls.add(f"candidate(tree_node({values!r}))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([0, 1, 2, 3, 4, 3, 4]))",
    "candidate(root=tree_node([25, 1, 3, 1, 3, 0, 2]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
