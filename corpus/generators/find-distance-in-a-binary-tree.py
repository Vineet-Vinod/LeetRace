import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 50)
        vals = rng.sample(range(0, 10**9 + 1), n)
        encoded: list[int | None] = vals[:]
        for j in range(1, n):
            if encoded[(j - 1) // 2] is None:
                encoded[j] = None
        nodes = [x for x in encoded if x is not None]
        p, q = rng.choices(nodes, k=2)
        calls.add(f"candidate(tree_node({encoded!r}), p={p}, q={q})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(root=tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), p=5, q=0)",
    "candidate(root=tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), p=5, q=5)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
