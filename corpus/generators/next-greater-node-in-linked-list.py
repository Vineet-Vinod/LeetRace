import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 1, 5), (2, 7, 4, 3, 5)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))))
    return [f"candidate(head=list_node({list(values)!r}))" for values in cases]
