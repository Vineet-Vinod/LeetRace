from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(root=tree_node([1, 2, 3]))",
    "candidate(root=tree_node([4, 2, 9, 3, 5, None, 7]))",
    "candidate(root=tree_node([21, 7, 14, 1, 1, 2, 2, 3, 3]))",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    values = [(i % 2001) - 1000 for i in range(10_000)]
    cases.add(f"candidate(root=tree_node({values!r}))")
    while len(cases) < 600:
        n = rng.randint(1, 30)
        vals = [rng.randint(-1000, 1000) for _ in range(n)]
        call = f"candidate(root=tree_node({vals!r}))"
        cases.add(call)
    return sorted(cases)
