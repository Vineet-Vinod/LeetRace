def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    calls = {f"candidate(root=tree_node({list(range(1, 101))!r}), x=99, y=100)"}
    while len(calls) < 600:
        n = rng.randint(2, 100)
        # tree_node consumes values in level order; this complete tree is valid.
        tree = list(range(1, n + 1))
        x, y = rng.sample(tree, 2)
        calls.add(f"candidate(root=tree_node({tree!r}), x={x}, y={y})")
    return sorted(calls)


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(root=tree_node([1, 2, 3, 4]), x=4, y=3)",
    "candidate(root=tree_node([1, 2, 3, None, 4, None, 5]), x=5, y=4)",
    "candidate(root=tree_node([1, 2, 3, None, 4]), x=2, y=3)",
]
_ORIGINAL_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    import ast

    calls = _ORIGINAL_GENERATE(seed) + _STATEMENT_EXAMPLE_CALLS
    unique = {}
    for call in calls:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        unique.setdefault(key, call)
    return [unique[key] for key in sorted(unique)]
