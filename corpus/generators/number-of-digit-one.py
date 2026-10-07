import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(n):
        assert 0 <= n <= 1000000000

    for n in [0, 1, 13, 1000000000]:
        add(n=n)
    for p in [10**i for i in range(1, 10)]:
        for n in [p - 1, p, p + 1]:
            if n <= 10**9:
                add(n=n)
    while len(calls) < 600:
        add(n=rng.randint(0, 1000000000))
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
