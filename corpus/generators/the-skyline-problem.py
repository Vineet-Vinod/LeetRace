import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(buildings):
        assert 1 <= len(buildings) <= 10000 and all(
            0 <= left < r <= 2**31 - 1 and 1 <= h <= 2**31 - 1
            for left, r, h in buildings
        )
        assert buildings == sorted(buildings, key=lambda x: x[0])

    add(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    add(buildings=[[0, 2, 3], [2, 5, 3]])
    while len(calls) < 597:
        n = rng.randint(1, 35)
        buildings = []
        mode = len(calls) % 3
        for i in range(n):
            left = rng.randint(0, 50)
            r = rng.randint(left + 1, 60)
            h = rng.randint(1, 100)
            if mode == 0:
                left = 2 * i
                r = left + 2
            if mode == 1:
                left = 0
                r = rng.randint(1, 100)
            buildings.append([left, r, h])
        buildings.sort(key=lambda x: x[0])
        add(buildings=buildings)
    calls["candidate(buildings=[[0,2147483647,2147483647]])"] = None
    calls["candidate(buildings=[[i,i+1,1] for i in range(10000)])"] = None
    calls["candidate(buildings=[[0,2147483647,2147483647]]*10000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
