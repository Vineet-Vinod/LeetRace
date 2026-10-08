import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10),
        (1, 3, 2, 7, 6, 5, 4),
        (1, 2, 3, 4, 5, 6),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        cases.add(tuple(rng.sample(range(1, 100001), n)))
    return [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
