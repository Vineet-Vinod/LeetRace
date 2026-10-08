import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(positions):
        assert 1 <= len(positions) <= 1000
        assert all(
            1 <= left <= 100000000 and 1 <= s <= 1000000 for left, s in positions
        )

    add(positions=[[1, 2], [2, 3], [6, 1]])
    add(positions=[[100, 100], [200, 100]])
    attempt = 0
    while len(calls) < 598:
        attempt += 1
        n = rng.randint(1, 35)
        mode = attempt % 4
        ps = [[rng.randint(1, 50), rng.randint(1, 20)] for _ in range(n)]
        if mode == 0:
            ps = [[1, rng.randint(1, 1000000)] for _ in range(n)]
        if mode == 1:
            ps = [[i * 20 + 1, 20] for i in range(n)]
        if mode == 2:
            ps = [
                [rng.randint(1, 100000000), rng.randint(1, 1000000)] for _ in range(n)
            ]
        add(positions=ps)
    calls["candidate(positions=[[1,1000000]]*1000)"] = None
    calls["candidate(positions=[[100000000,1000000]])"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
