import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["nums"]
        assert (
            1 <= len(a) <= 100000
            and all(1 <= v <= 10**9 for v in a)
            and 1 <= d["y"] < d["x"] <= 10**9
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

    add(nums=[3, 4, 1, 7, 6], x=4, y=2)
    add(nums=[1, 2, 1], x=2, y=1)
    add(nums=[10**9] * 100000, x=2, y=1)
    add(nums=[10**9], x=10**9, y=10**9 - 1)
    add(nums=[1] * 100000, x=10**9, y=1)
    t = 0
    while len(calls) < 600:
        y = rng.randint(1, 100)
        x = rng.randint(y + 1, 1000)
        add(nums=[rng.randint(1, 10000) for _ in range(rng.randint(1, 35))], x=x, y=y)
        t += 1
    return calls
