def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    max_chain = [(-15000 + i) for i in range(30000)]
    cases = {
        "candidate(root=tree_node([1, None, 3, 2, 4, None, None, None, 5]))",
        "candidate(root=tree_node([2, None, 3, 2, None, 1]))",
    }
    # Encode a right-only chain in level order and cover the maximum node count.
    max_tree = [max_chain[0]]
    for value in max_chain[1:]:
        max_tree.extend([None, value])
    cases.add(f"candidate(root=tree_node({max_tree!r}))")
    while len(cases) < 600:
        length = rng.randint(1, 80)
        if rng.random() < 0.7:
            start = rng.randint(-30000, 30000 - length + 1)
            chain = list(range(start, start + length))
            tree = [chain[0]]
            for value in chain[1:]:
                tree.extend([None, value])
        else:
            n = rng.randint(1, 80)
            tree = [rng.randint(-30000, 30000) for _ in range(n)]
            for i in range(n):
                if rng.random() < 0.15:
                    tree[2 * i + 1 : 2 * i + 2] = [None]
                if rng.random() < 0.15:
                    tree[2 * i + 2 : 2 * i + 3] = [None]
            while tree and tree[-1] is None:
                tree.pop()
        assert sum(value is not None for value in tree) <= 30000
        assert all(value is None or -30000 <= value <= 30000 for value in tree)
        cases.add(f"candidate(root=tree_node({tree!r}))")
    return sorted(cases)
