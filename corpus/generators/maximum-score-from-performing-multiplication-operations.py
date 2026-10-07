import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["nums"]
        b = d["multipliers"]
        assert (
            1 <= len(b) <= 300
            and len(b) <= len(a) <= 100000
            and all(-1000 <= v <= 1000 for v in a + b)
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

    add(nums=[1, 2, 3], multipliers=[3, 2, 1])
    add(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6])
    add(nums=[-1000, 1000] * 50000, multipliers=[-1000, 1000] * 150)
    add(nums=[1000] * 300, multipliers=[1000] * 300)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 30)
        m = rng.randint(1, n)
        a = [rng.randint(-1000, 1000) for _ in range(n)]
        b = [rng.randint(-1000, 1000) for _ in range(m)]
        if t % 5 == 0:
            b = [rng.choice([-1000, 0, 1000])] * m
        add(nums=a, multipliers=b)
        t += 1
    return calls
