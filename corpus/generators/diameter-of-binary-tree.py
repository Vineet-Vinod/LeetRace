import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1,), (1, 2), (1, 2, 3, 4, 5)}
    cases.add(tuple([100, -100] * 5000))
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        cases.add(tuple(rng.randint(-100, 100) for _ in range(size)))
    calls = [f"candidate(root=tree_node({list(values)!r}))" for values in cases]
    calls.extend(
        [
            "candidate(root=tree_node([1, 2, 3, 4, 5]))",
            "candidate(root=tree_node([1, 2]))",
        ]
    )
    return list(dict.fromkeys(calls))
