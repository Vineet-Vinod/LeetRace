import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (3, 2, 3, None, 3, None, 1),
        (3, 4, 5, 1, 3, None, 1),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(tuple(rng.randint(0, 10000) for _ in range(n)))
    return [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
