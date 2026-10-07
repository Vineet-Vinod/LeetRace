import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(m, n):
        assert 1 <= m <= 5 and 1 <= n <= 1000

    for m in range(1, 6):
        for n in range(1, 101):
            add(m=m, n=n)
        add(m=m, n=1000)
    while len(calls) < 600:
        add(m=rng.randint(1, 5), n=rng.randint(101, 1000))
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
