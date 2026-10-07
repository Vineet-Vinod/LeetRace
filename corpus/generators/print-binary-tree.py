import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 63)
        values = rng.sample(range(-99, 100), n)
        encoded: list[int | None] = values
        for i in range(1, n):
            if encoded[(i - 1) // 2] is None:
                encoded[i] = None
        while encoded and encoded[-1] is None:
            encoded.pop()
        calls.add(f"candidate(tree_node({encoded!r}))")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([1, 2, 3, None, 4]))",
    "candidate(root=tree_node([1, 2]))",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
