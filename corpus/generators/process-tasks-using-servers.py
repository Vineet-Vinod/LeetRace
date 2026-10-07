import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((3, 3, 2), (1, 2, 3, 2, 1, 2)),
        ((5, 1, 4, 3, 2), (2, 1, 2, 4, 5, 2, 1)),
        ((1,), (1, 2, 3)),
    }
    cases.add(((1,) * 200_000, (1,) * 200_000))
    while len(cases) < 600:
        servers = tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 30)))
        tasks = tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 60)))
        cases.add((servers, tasks))
    assert all(
        1 <= len(servers) <= 200_000
        and 1 <= len(tasks) <= 200_000
        and all(1 <= weight <= 200_000 for weight in servers)
        and all(1 <= duration <= 200_000 for duration in tasks)
        for servers, tasks in cases
    )
    return [
        f"candidate(servers={list(servers)!r}, tasks={list(tasks)!r})"
        for servers, tasks in sorted(cases)
    ]
