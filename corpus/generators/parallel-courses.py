import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (3, ((1, 3), (2, 3))),
        (3, ((1, 2), (2, 3), (3, 1))),
        (5000, tuple((i, i + 1) for i in range(1, 5000)) + ((1, 5000),)),
    }
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edges = set()
        if rng.random() < 0.8:
            order = list(range(1, n + 1))
            rng.shuffle(order)
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.random() < 0.07:
                        edges.add((order[i], order[j]))
        elif n > 1:
            target = rng.randint(1, min(50, n * (n - 1)))
            while len(edges) < target:
                edges.add(tuple(rng.sample(range(1, n + 1), 2)))
        if not edges:
            edges.add(tuple(rng.sample(range(1, n + 1), 2)))
        cases.add((n, tuple(sorted(edges))))
    assert len(cases) == 600 and all(
        1 <= n <= 5000
        and 1 <= len(e) <= 5000
        and all(1 <= a <= n and 1 <= b <= n and a != b for a, b in e)
        for n, e in cases
    )
    return [
        f"candidate(n={n}, relations={[list(edge) for edge in edges]!r})"
        for n, edges in sorted(cases)
    ]
