def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([10,4,6]))",
        "candidate(root=tree_node([10,4,4]))",
    }
    while len(calls) < 600:
        root = rng.randint(10, 100)
        left = rng.randint(1, root - 1)
        right = root - left
        calls.add(f"candidate(root=tree_node([{root},{left},{right}]))")
        calls.add(f"candidate(root=tree_node([{root},{left},{right + 1}]))")
    return sorted(calls)


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(root=tree_node([10, 4, 6]))",
    "candidate(root=tree_node([5, 3, 1]))",
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
