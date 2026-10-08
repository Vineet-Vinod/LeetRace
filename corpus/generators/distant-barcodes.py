import random
from collections import Counter


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 1, 1, 2, 2, 2), (1, 1, 1, 1, 2, 2, 3, 3)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        values = [rng.randint(1, 20) for _ in range(n)]
        if max(Counter(values).values()) <= (n + 1) // 2:
            cases.add(tuple(values))
    return [f"candidate(barcodes={list(values)!r})" for values in cases]
