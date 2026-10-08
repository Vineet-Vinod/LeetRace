def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(root=tree_node([4,2,6,3,1,5]), val=1, depth=2)",
        "candidate(root=tree_node([1]), val=9, depth=1)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 35)
        vals = [rng.randint(-100, 100) for _ in range(n)]
        tree = vals[:]
        tree.extend([None] * (2 * n + 1))
        for i in range(n):
            if rng.random() < 0.2:
                tree[2 * i + 1] = None
            if rng.random() < 0.2:
                tree[2 * i + 2] = None
        while tree and tree[-1] is None:
            tree.pop()
        if tree[0] is None:
            tree[0] = vals[0]
        depth = rng.randint(1, max(1, n.bit_length() + 1))
        cases.add(
            f"candidate(root=tree_node({tree!r}), val={rng.randint(-100000, 100000)}, depth={depth})"
        )
    return sorted(cases)
