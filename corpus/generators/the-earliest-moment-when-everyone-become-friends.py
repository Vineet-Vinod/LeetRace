import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    complete_logs = tuple(
        (timestamp, first, second)
        for timestamp, (first, second) in enumerate(
            (
                (first, second)
                for first in range(100)
                for second in range(first + 1, 100)
            )
        )
    )
    cases: set[tuple[int, tuple[tuple[int, int, int], ...]]] = {
        (2, ((0, 0, 1),)),
        (3, ((0, 0, 1), (1, 1, 2))),
        (4, ((0, 0, 1), (1, 2, 3))),
        (2, ((10**9, 0, 1),)),
        (100, complete_logs),
    }
    while len(cases) < 600:
        n = rng.randint(2, 30)
        edges: set[tuple[int, int]] = set()
        for person in range(1, n):
            other = rng.randrange(person)
            edges.add((other, person))
        all_edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(all_edges)
        for pair in all_edges:
            if len(edges) >= rng.randint(n - 1, min(len(all_edges), n + 10)):
                break
            edges.add(pair)
        logs = tuple(
            sorted(
                (timestamp, a, b)
                for timestamp, (a, b) in enumerate(
                    sorted(edges), start=rng.randint(0, 1000)
                )
            )
        )
        if len(logs) > 1 and rng.random() < 0.2:
            logs = logs[:-1]
        cases.add((n, logs))
    assert all(
        2 <= n <= 100
        and 1 <= len(logs) <= 10_000
        and len({t for t, _, _ in logs}) == len(logs)
        and len({(min(a, b), max(a, b)) for _, a, b in logs}) == len(logs)
        and all(
            0 <= t <= 10**9 and 0 <= a < n and 0 <= b < n and a != b for t, a, b in logs
        )
        for n, logs in cases
    )
    return [
        f"candidate(logs={[[t, a, b] for t, a, b in logs]!r}, n={n})"
        for n, logs in sorted(cases)
    ]
