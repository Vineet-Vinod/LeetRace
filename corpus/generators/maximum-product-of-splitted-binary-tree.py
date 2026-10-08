import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 2, 3, 4, 5, 6),
        (1, None, 2, 3, 4, None, None, 5, 6),
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10000) for _ in range(rng.randint(2, 80))))
    return [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
