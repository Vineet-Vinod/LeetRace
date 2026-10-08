import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        tasks = kwargs["tasks"]
        assert 1 <= len(tasks) <= 100000 and all(
            len(t) == 2 and 1 <= t[0] <= t[1] <= 10000 for t in tasks
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(tasks=[[10000, 10000]] * 100000)
    add(tasks=[[1, 10000]] * 100000)
    add(tasks=[[1, 2], [2, 4], [4, 8]])
    add(tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]])
    add(tasks=[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]])
    while len(calls) < 600:
        tasks = []
        for _ in range(rng.randint(1, 35)):
            actual = rng.randint(1, 10000)
            minimum = rng.randint(actual, 10000)
            tasks.append([actual, minimum])
        add(tasks=tasks)
    return calls
