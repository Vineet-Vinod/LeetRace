import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(s, k):
        assert (
            1 <= len(s) <= 10000
            and set(s) <= set("abcdefghijklmnopqrstuvwxyz")
            and 1 <= k <= 26
        )

    add(s="accca", k=2)
    add(s="aabaab", k=3)
    add(s="xxyz", k=1)
    while len(calls) < 598:
        alphabet = "abcdefghijklmnopqrstuvwxyz"[: rng.randint(1, 10)]
        s = "".join(rng.choices(alphabet, k=rng.randint(1, 40)))
        k = rng.randint(1, 26)
        if len(calls) % 3 == 0:
            k = rng.randint(1, min(5, len(alphabet)))
        add(s=s, k=k)
    calls['candidate(s="a"*10000, k=1)'] = None
    calls['candidate(s="abcdefghijklmnopqrstuvwxyz"*384+"abcdefghijklmnop", k=26)'] = (
        None
    )
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
