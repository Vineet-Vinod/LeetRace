import random

DOMAIN_SIZE = 100


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(n):
        assert 1 <= n <= 100

    # One integer in [1,100] is the full legal domain: exactly 100 calls.
    for n in range(1, 101):
        add(n=n)
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
