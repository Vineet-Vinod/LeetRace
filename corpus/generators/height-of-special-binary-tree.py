import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()

    def add_tree(values: list[int | None]) -> None:
        node_values = [value for value in values if value is not None]
        assert 2 <= len(node_values) <= 10_000
        assert len(node_values) == len(set(node_values))
        assert all(1 <= value <= len(node_values) for value in node_values)
        cases.add(f"candidate(root=link_special_tree_leaves(tree_node({values!r})))")

    add_tree([1, 2, 3, None, None, 4, 5])
    add_tree([1, 2])
    add_tree([1, 2, 3, None, None, 4, None, 5, 6])
    add_tree([1, None, 2])

    add_tree(list(range(1, 10_001)))
    right_chain: list[int | None] = []
    left_chain: list[int | None] = [1]
    for value in range(1, 10_001):
        right_chain.extend((value, None))
    for value in range(2, 10_001):
        left_chain.extend((value, None))
    right_chain.pop()
    left_chain.pop()
    add_tree(right_chain)
    add_tree(left_chain)

    while len(cases) < 600:
        count = rng.randint(2, 300)
        labels = rng.sample(range(1, count + 1), count)
        add_tree(labels)
    return sorted(cases)
