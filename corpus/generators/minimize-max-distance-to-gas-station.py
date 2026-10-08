import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        s, k = kw["stations"], kw["k"]
        assert (
            10 <= len(s) <= 2000
            and all(0 <= x <= 10**8 for x in s)
            and all(a < b for a, b in zip(s, s[1:]))
        )
        assert 1 <= k <= 10**6
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"stations": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "k": 9},
        {"stations": [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], "k": 1},
    ] + [
        {"stations": [i * 50000 for i in range(1999)] + [10**8], "k": 1000000},
        {"stations": list(range(10)), "k": 1},
        {"stations": list(range(9)) + [10**8], "k": 1},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(10, 30)
        if len(calls) % 3 == 0:
            gap = rng.randint(1, 10000)
            start = rng.randint(0, 1000)
            s = [start + i * gap for i in range(n)]
        else:
            s = sorted(rng.sample(range(100000), n))
        k = rng.randint(1, 1000)
        add(stations=s, k=k)
    return calls
