import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(s, queryCharacters, queryIndices):
        assert (
            1 <= len(s) <= 100000
            and 1 <= len(queryCharacters) == len(queryIndices) <= 100000
        )
        assert set(s + queryCharacters) <= set("abcdefghijklmnopqrstuvwxyz") and all(
            0 <= i < len(s) for i in queryIndices
        )

    add(s="babacc", queryCharacters="bcb", queryIndices=[1, 3, 3])
    while len(calls) < 598:
        n = rng.randint(1, 40)
        q = rng.randint(1, 40)
        s = "".join(rng.choices("abc", k=n))
        if len(calls) % 3 == 0:
            s = "a" * n
        indices = [rng.randrange(n) for _ in range(q)]
        chars = "".join(rng.choices("abc", k=q))
        add(s=s, queryCharacters=chars, queryIndices=indices)
    calls['candidate(s="a"*100000, queryCharacters="b", queryIndices=[50000])'] = None
    calls['candidate(s="ab", queryCharacters="ab"*50000, queryIndices=[0,1]*50000)'] = (
        None
    )
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
