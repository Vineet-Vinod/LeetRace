import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1,),
        (2, 3, 4),
        (2, 2, 2, 2, 2, 2, 2),
        (6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4),
        (2,) * 10_000,
        (100,) * 10_000,
    }
    while len(cases) < 600:
        size = rng.randint(1, 127)
        values = tuple(rng.randint(1, 100) for _ in range(size))
        cases.add(values)
    assert all(
        1 <= len(tree) <= 10_000
        and all(value is None or 1 <= value <= 100 for value in tree)
        for tree in cases
    )
    return [
        f"candidate(root=tree_node({list(tree)!r}))" for tree in sorted(cases, key=repr)
    ]
