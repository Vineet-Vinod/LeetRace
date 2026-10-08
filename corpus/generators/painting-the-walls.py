import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["cost"]
        b = d["time"]
        assert (
            1 <= len(a) <= 500
            and len(a) == len(b)
            and all(1 <= v <= 10**6 for v in a)
            and all(1 <= v <= 500 for v in b)
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

    add(cost=[1, 2, 3, 2], time=[1, 2, 3, 2])
    add(cost=[2, 3, 4, 2], time=[1, 1, 1, 1])
    add(cost=[10**6] * 500, time=[1] * 500)
    add(cost=[10**6] * 500, time=[500] * 500)
    add(cost=[1] * 500, time=[1] * 500)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 30)
        cost = [rng.randint(1, 1000) for _ in range(n)]
        time = [rng.randint(1, 30) for _ in range(n)]
        if t % 4 == 0:
            time = [1] * n
        add(cost=cost, time=time)
        t += 1
    return calls
