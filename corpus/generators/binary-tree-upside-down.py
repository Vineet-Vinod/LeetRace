import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(), (1,), (1, 2, 3, 4, 5)}
    while len(cases) < 600:
        depth = rng.choice((2, 3))
        # At most two spine levels keep every right child a leaf.
        values = tuple(rng.sample(range(1, 11), 3 if depth == 2 else 5))
        cases.add(values)

    def tree(values: tuple[int, ...]) -> str:
        return f"tree_node({list(values)!r})"

    return [f"candidate(root={tree(values)})" for values in cases]
