import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        ((1, 2), (2, 4), (3, 2), (4, 1)),
        ((7, 10), (7, 12), (7, 5), (7, 4), (7, 2)),
        ((1, 1),),
        ((10**9, 10**9),) * 100_000,
    }
    while len(cases) < 600:
        tasks = tuple(
            (rng.randint(1, 1000), rng.randint(1, 1000))
            for _ in range(rng.randint(1, 70))
        )
        cases.add(tasks)
    assert all(
        1 <= len(tasks) <= 100_000
        and all(
            1 <= enqueue <= 10**9 and 1 <= duration <= 10**9
            for enqueue, duration in tasks
        )
        for tasks in cases
    )
    return [
        f"candidate(tasks={[[a, b] for a, b in tasks]!r})" for tasks in sorted(cases)
    ]
