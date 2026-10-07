import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(d, low, high):
        assert 0 <= d <= 9 and 1 <= low <= high <= 200000000

    for d in range(10):
        for p in [1, 10, 100, 1000, 10000, 10000000, 100000000]:
            add(d=d, low=max(1, p - 1), high=min(200000000, p + 1))
        add(d=d, low=1, high=200000000)
    while len(calls) < 600:
        low = rng.randint(1, 200000000)
        high = rng.randint(low, 200000000)
        add(d=rng.randrange(10), low=low, high=high)
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
