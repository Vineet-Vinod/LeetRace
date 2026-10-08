import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 2, 3, 2), (2, 1, 1, 2), (3, 2, 2, 1, 3, 2, 4)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(head=list_node({list(values)!r}))" for values in cases]
