import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(word, k):
        assert (
            1 <= len(word) <= 1000000
            and 1 <= k <= len(word)
            and set(word) <= set("abcdefghijklmnopqrstuvwxyz")
        )

    add(word="abacaba", k=3)
    add(word="abacaba", k=4)
    add(word="abcbabcd", k=2)
    while len(calls) < 598:
        n = rng.randint(1, 100)
        word = "".join(rng.choices("abc", k=n))
        if len(calls) % 3 == 0:
            word = ("ab" * n)[:n]
        add(word=word, k=rng.randint(1, n))
    calls['candidate(word="a"*1000000, k=1)'] = None
    calls['candidate(word="a"*999999+"b", k=1)'] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
