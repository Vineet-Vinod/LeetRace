import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        tasks = kwargs["tasks"]
        assert 1 <= len(tasks) <= 2000 and all(
            len(t) == 3 and 1 <= t[0] <= t[1] <= 2000 and 1 <= t[2] <= t[1] - t[0] + 1
            for t in tasks
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(tasks=[[1, i, i] for i in range(1, 2001)])
    add(tasks=[[1, 2000, 1]] * 2000)
    add(tasks=[[2, 3, 1], [4, 5, 1], [1, 5, 2]])
    add(tasks=[[1, 3, 2], [2, 5, 3], [5, 6, 2]])
    while len(calls) < 600:
        tasks = []
        limit = rng.choice([8, 30, 2000])
        for _ in range(rng.randint(1, 25)):
            start = rng.randint(1, limit)
            end = rng.randint(start, limit)
            tasks.append([start, end, rng.randint(1, end - start + 1)])
        add(tasks=tasks)
    return calls
