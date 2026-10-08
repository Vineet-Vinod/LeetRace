def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    calls = {
        "candidate(root1=tree_node([3,5,1,6,2,9,8,None,None,7,4]), root2=tree_node([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]))",
        "candidate(root1=tree_node([1,2,3]), root2=tree_node([1,3,2]))",
        f"candidate(root1=tree_node({list(range(1, 201))!r}), root2=tree_node({list(range(1, 201))!r}))",
    }
    while len(calls) < 600:
        n1, n2 = rng.randint(1, 30), rng.randint(1, 30)
        a = list(range(1, n1 + 1))
        b = list(range(101, 101 + n2))
        if rng.random() < 0.5:
            b = a[:]
        calls.add(f"candidate(root1=tree_node({a!r}), root2=tree_node({b!r}))")
    return sorted(calls)


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(root1=tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]), root2=tree_node([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]))",
    "candidate(root1=tree_node([1, 2, 3]), root2=tree_node([1, 3, 2]))",
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
