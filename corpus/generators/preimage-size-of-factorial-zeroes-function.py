import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        assert 0 <= d["k"] <= 10**9

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

    add(k=0)
    add(k=5)
    add(k=3)
    add(k=10**9)
    for exponent in range(1, 14):
        k = sum(5**j for j in range(exponent))
        for delta in (-1, 0, 1):
            if 0 <= k + delta <= 10**9:
                add(k=k + delta)
    t = 0
    while len(calls) < 600:
        if t < 300:
            k = t
        else:
            k = rng.randint(0, 10**9)
        add(k=k)
        t += 1
    return calls
