import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    valid_trees = set()
    invalid_trees = set()

    def make_valid(n: int) -> list[int | None]:
        values = sorted(rng.sample(range(-1000, 1001), n))
        tree: list[int | None] = [None] * n
        next_value = 0

        def fill(index: int) -> None:
            nonlocal next_value
            if index >= n:
                return
            fill(index * 2 + 1)
            tree[index] = values[next_value]
            next_value += 1
            fill(index * 2 + 2)

        fill(0)
        return tree

    while len(valid_trees) < 300:
        n = rng.randint(1, 30)
        valid_trees.add(tuple(make_valid(n)))
    while len(invalid_trees) < 300:
        n = rng.randint(4, 30)
        tree = make_valid(n)
        if rng.random() < 0.5:
            tree[3] = 2001
        elif n > 5:
            tree[5] = -2001
        else:
            tree[3] = 2001
        invalid_trees.add(tuple(tree))

    calls = [
        f"candidate(root=tree_node({list(tree)!r}))" for tree in sorted(valid_trees)
    ]
    calls.extend(
        f"candidate(root=tree_node({list(tree)!r}))" for tree in sorted(invalid_trees)
    )
    n = 10000
    values = list(range(-5000, 5000))
    max_tree: list[int | None] = [None] * n
    next_value = 0

    def fill_max(index: int) -> None:
        nonlocal next_value
        if index >= n:
            return
        fill_max(2 * index + 1)
        max_tree[index] = values[next_value]
        next_value += 1
        fill_max(2 * index + 2)

    fill_max(0)
    calls.append(f"candidate(root=tree_node({max_tree!r}))")
    invalid_max = max_tree.copy()
    invalid_max[1] = 2**31 - 1
    calls.append(f"candidate(root=tree_node({invalid_max!r}))")
    calls.append("candidate(root=tree_node([0, -2147483648, 2147483647]))")
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    assert len(valid_trees) == len(invalid_trees) == 300
    return calls
