import random


def traversals(tree: list[int | None], index: int = 0) -> tuple[list[int], list[int]]:
    if index >= len(tree) or tree[index] is None:
        return [], []
    value = tree[index]
    left_pre, left_post = traversals(tree, 2 * index + 1)
    right_pre, right_post = traversals(tree, 2 * index + 2)
    return [value] + left_pre + right_pre, left_post + right_post + [value]


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: preorder/postorder represent the same tree with unique values, n 1..30."""
    rng = random.Random(seed)
    calls = {
        "candidate(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1])",
        "candidate(preorder=[1], postorder=[1])",
    }
    while len(calls) < 600:
        size = rng.randint(1, 30)
        values = rng.sample(range(1, size + 1), size)
        tree: list[int | None] = [values[0]]
        available = [0]
        for value in values[1:]:
            parent = rng.choice(available)
            left, right = 2 * parent + 1, 2 * parent + 2
            while len(tree) <= right:
                tree.append(None)
            slot = (
                left
                if tree[left] is None
                and (tree[right] is not None or rng.random() < 0.5)
                else right
            )
            tree[slot] = value
            if tree[left] is not None and tree[right] is not None:
                available.remove(parent)
            available.append(slot)
        preorder, postorder = traversals(tree)
        calls.add(f"candidate(preorder={preorder!r}, postorder={postorder!r})")
    return sorted(calls)
