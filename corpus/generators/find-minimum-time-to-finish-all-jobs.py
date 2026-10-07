import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        jobs, k = values["jobs"], values["k"]
        assert 1 <= k <= len(jobs) <= 12 and all(1 <= x <= 10000000 for x in jobs)
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for jobs, k in [
        ([3, 2, 3], 3),
        ([1, 2, 4, 7, 8], 2),
        ([10000000] * 12, 1),
        ([10000000] * 12, 12),
        ([1] * 12, 5),
        ([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1], 4),
    ]:
        emit(jobs=jobs, k=k)
    while len(calls) < 600:
        n = rng.randint(1, 10)
        emit(jobs=[rng.randint(1, 100) for _ in range(n)], k=rng.randint(1, n))
    return calls
