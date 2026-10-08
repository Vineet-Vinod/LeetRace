import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (4, ((0, 1, 1), (1, 2, 3), (2, 3, 2), (0, 3, 4)), 0, (2, 3)),
        (5, ((0, 1, 2), (0, 2, 4), (1, 3, 1), (2, 3, 3), (3, 4, 2)), 1, (0, 4)),
    }
    while len(cases) < 600:
        n = rng.randint(2, 40)
        edge_set: set[tuple[int, int, int]] = set()
        for source in range(n):
            for target in range(n):
                if source != target and rng.random() < 0.08:
                    edge_set.add((source, target, rng.randint(1, 1000)))
        if not edge_set:
            source = rng.randrange(n)
            target = (source + 1) % n
            edge_set.add((source, target, rng.randint(1, 1000)))
        s = rng.randrange(n)
        marked = tuple(
            rng.sample([node for node in range(n) if node != s], rng.randint(1, n - 1))
        )
        cases.add((n, tuple(sorted(edge_set)), s, marked))
    return [
        f"candidate(n={n}, edges={[list(e) for e in edges]!r}, s={s}, marked={list(marked)!r})"
        for n, edges, s, marked in cases
    ]
