def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    trees = {
        (),
        (1,),
        (1, 2, 3),
        (1, 2, None, 3, None, 4),
        tuple((i % 2001) - 1000 for i in range(100000)),
    }
    while len(trees) < 600:
        n = rng.randint(1, 60)
        trees.add(tuple(rng.sample(range(-1000, 1001), n)))
    return [f"candidate(root=tree_node({list(t)!r}))" for t in sorted(trees, key=repr)]


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(root=tree_node([3, 9, 20, None, None, 15, 7]))",
    "candidate(root=tree_node([2, None, 3, None, 4, None, 5, None, 6]))",
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
