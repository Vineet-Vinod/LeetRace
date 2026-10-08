import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(events, k):
        assert 1 <= k <= len(events) and k * len(events) <= 1000000
        assert all(1 <= s <= e <= 10**9 and 1 <= v <= 1000000 for s, e, v in events)

    add(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2)
    while len(calls) < 597:
        n = rng.randint(1, 35)
        mode = len(calls) % 4
        es = []
        for i in range(n):
            a = rng.randint(1, 50)
            b = rng.randint(a, 60)
            if mode == 0:
                a = b = i + 1
            if mode == 1:
                a = 1
                b = 100
            es.append([a, b, rng.randint(1, 1000000)])
        add(events=es, k=rng.randint(1, n))
    calls["candidate(events=[[1,1000000000,1000000]], k=1)"] = None
    calls["candidate(events=[[i,i,1] for i in range(1,1001)], k=1000)"] = None
    calls["candidate(events=[[1,1,1]]*1000000, k=1)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
