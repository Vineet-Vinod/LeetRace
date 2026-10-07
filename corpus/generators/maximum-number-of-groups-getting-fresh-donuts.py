import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["groups"]
        assert (
            1 <= d["batchSize"] <= 9
            and 1 <= len(a) <= 30
            and all(1 <= v <= 10**9 for v in a)
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(batchSize=3, groups=[1, 2, 3, 4, 5, 6])
    add(batchSize=4, groups=[1, 3, 2, 5, 2, 2, 1, 6])
    add(batchSize=9, groups=[1, 2, 3, 4] * 7 + [1, 2])
    add(batchSize=9, groups=[10**9] * 30)
    add(batchSize=1, groups=[10**9] * 30)
    t = 0
    while len(calls) < 600:
        b = rng.randint(1, 9)
        n = rng.randint(1, 12)
        groups = [rng.randint(1, 1000) for _ in range(n)]
        if t % 4 == 0:
            groups = [b * rng.randint(1, 100) for _ in range(n)]
        add(batchSize=b, groups=groups)
        t += 1
    return calls
