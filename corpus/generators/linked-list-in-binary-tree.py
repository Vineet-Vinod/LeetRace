import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(head, tree):
        key = (tuple(head), tuple(tree))
        if key not in seen:
            assert 1 <= len(head) <= 100 and 1 <= len(tree) <= 2500
            assert all(1 <= v <= 100 for v in head + tree)
            seen.add(key)
            cases.append(
                f"candidate(head=list_node({head!r}), root=tree_node({tree!r}))"
            )

    for n in range(3, 100):
        tree = [(i % 90) + 1 for i in range(n)]
        path = [tree[i] for i in [0, 1, 3, 7, 15] if i < n]
        add(path, tree)
        add([100, 100], tree)
    for _ in range(300):
        n = r.randint(40, 100)
        tree = [r.randint(1, 80) for _ in range(n)]
        # Write a guaranteed root-to-left path, filling its heap-indexed ancestors.
        depth = r.randint(1, 5)
        path = [r.randint(1, 80) for _ in range(depth + 1)]
        for j, value in enumerate(path):
            tree[(1 << j) - 1] = value
        add(path, tree)
    for _ in range(300):
        n = r.randint(40, 100)
        tree = [r.randint(1, 80) for _ in range(n)]
        head = [r.randint(81, 100) for _ in range(r.randint(2, 12))]
        add(head, tree)
    add([1] * 100, [i % 100 + 1 for i in range(2500)])
    return cases
