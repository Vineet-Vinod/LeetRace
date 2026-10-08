import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int | None, ...], int]] = {
        ((1,), 1),
        ((1, 3, 2), 1),
        ((1, 2, 3, 4, None, None, None, 5, None, 6), 2),
    }
    while len(cases) < 600:
        n = rng.randint(1, 40)
        values = rng.sample(range(1, 1001), n)
        # A complete-prefix level-order tree is valid, has unique values, and keeps both dimensions legal.
        tree = tuple(values)
        cases.add((tree, rng.choice(values)))
    return [f"candidate(root=tree_node({list(tree)!r}), k={k})" for tree, k in cases]
