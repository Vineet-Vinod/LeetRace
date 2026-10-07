import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((5, 4, 3, 2, 1), (1, 1, 2, 2, 3), 3, 1),
        ((5, 4, 3, 2, 1), (1, 3, 3, 3, 2), 3, 2),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        values = tuple(rng.randint(0, 20000) for _ in range(n))
        labels = tuple(rng.randint(0, 20000) for _ in range(n))
        cases.add((values, labels, rng.randint(1, n), rng.randint(1, n)))
    return [
        f"candidate(values={list(v)!r}, labels={list(label_list)!r}, numWanted={w}, useLimit={limit})"
        for v, label_list, w, limit in cases
    ]
