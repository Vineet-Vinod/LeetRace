import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        values = [rng.randint(-100, 100) for _ in range(rng.randint(0, 200))]
        x = rng.randint(-200, 200)
        calls.add(f"candidate(list_node({values!r}), x={x})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(head=list_node([1, 4, 3, 2, 5, 2]), x=3)",
    "candidate(head=list_node([2, 1]), x=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
