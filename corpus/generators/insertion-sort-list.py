import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(4, 2, 1, 3), (-1, 5, 3, 4, 0), (1,)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(-5000, 5000) for _ in range(rng.randint(1, 100))))
    return [f"candidate(head=list_node({list(values)!r}))" for values in cases]
