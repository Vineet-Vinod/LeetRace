def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(root1=tree_node([]), root2=tree_node([]))"])

    # Construct BSTs by inserting unique values, then encode their level-order values.
    def tree(values):
        if not values:
            return []
        nodes = []
        sorted_values = sorted(set(values))

        def fill(items):
            if not items:
                return []
            mid = len(items) // 2
            left = fill(items[:mid])
            right = fill(items[mid + 1 :])
            return [items[mid], left, right]

        # A balanced BST encoded in nested form is flattened in level order.
        nested = fill(sorted_values)
        from collections import deque

        pending = deque([nested])
        while pending:
            item = pending.popleft()
            if not item:
                nodes.append(None)
                continue
            value, left, right = item
            nodes.append(value)
            pending.extend((left, right))
        while nodes and nodes[-1] is None:
            nodes.pop()
        return nodes

    cases.add("candidate(root1=tree_node([-100000]), root2=tree_node([100000]))")
    maximum_tree = tree(list(range(-2500, 2500)))
    cases.add(
        f"candidate(root1=tree_node({maximum_tree!r}), root2=tree_node({maximum_tree!r}))"
    )
    for index in range(600):
        size1 = index % 35
        size2 = (index * 11) % 35
        vals1 = rng.sample(range(-100000, 100001), size1)
        vals2 = rng.sample(range(-100000, 100001), size2)
        a, b = tree(vals1), tree(vals2)
        cases.add(f"candidate(root1=tree_node({a!r}), root2=tree_node({b!r}))")
    if (
        "all-elements-in-two-binary-search-trees"
        == "determine-color-of-a-chessboard-square"
    ):
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "all-elements-in-two-binary-search-trees" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        a = tree(rng.sample(range(-1000, 1001), rng.randrange(0, 15)))
        b = tree(rng.sample(range(-1000, 1001), rng.randrange(0, 15)))
        cases.add(f"candidate(root1=tree_node({a!r}), root2=tree_node({b!r}))")
    return sorted(cases)
