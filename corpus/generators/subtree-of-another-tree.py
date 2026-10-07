def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([3,4,5,1,2]), subRoot=tree_node([4,1,2]))",
        "candidate(root=tree_node([1,2,3]), subRoot=tree_node([2,1]))",
        f"candidate(root=tree_node({list(range(1, 2001))!r}), subRoot=tree_node({list(range(1, 1001))!r}))",
    }
    while len(calls) < 600:
        n = rng.randint(1, 40)
        m = rng.randint(1, 15)
        root = list(rng.randint(0, 100) for _ in range(n))
        sub = list(rng.randint(0, 100) for _ in range(m))
        if rng.random() < 0.5 and m <= n:
            start = rng.randint(0, n - m)
            root[start : start + m] = sub
        calls.add(f"candidate(root=tree_node({root!r}), subRoot=tree_node({sub!r}))")
    for size in range(1, 101):
        root = list(range(1, size + 1))
        start = rng.randrange(size)
        pending = [start]
        sub = []
        while pending:
            index = pending.pop(0)
            if index >= size:
                sub.append(None)
                continue
            sub.append(root[index])
            pending.extend((2 * index + 1, 2 * index + 2))
        while sub and sub[-1] is None:
            sub.pop()
        calls.add(f"candidate(root=tree_node({root!r}), subRoot=tree_node({sub!r}))")
        absent = sub[:]
        absent[0] = 10000
        calls.add(f"candidate(root=tree_node({root!r}), subRoot=tree_node({absent!r}))")
    return sorted(calls)


_STATEMENT_EXAMPLE_CALLS = [
    "candidate(root=tree_node([3, 4, 5, 1, 2]), subRoot=tree_node([4, 1, 2]))",
    "candidate(root=tree_node([3, 4, 5, 1, 2, None, None, None, None, 0]), subRoot=tree_node([4, 1, 2]))",
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
