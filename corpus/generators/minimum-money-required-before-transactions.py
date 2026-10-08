import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["transactions"]
        assert 1 <= len(a) <= 100000 and all(
            len(p) == 2 and all(0 <= x <= 10**9 for x in p) for p in a
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(transactions=[[2, 1], [5, 0], [4, 2]])
    add(transactions=[[3, 0], [0, 3]])
    add(transactions=[[10**9, 0]] * 100000)
    add(transactions=[[0, 10**9]] * 100000)
    add(transactions=[[2, 1], [5, 0], [4, 2]])
    add(transactions=[[3, 0], [0, 3]])
    while len(calls) < 600:
        a = [
            [rng.randint(0, 100), rng.randint(0, 100)]
            for _ in range(rng.randint(1, 60))
        ]
        if len(calls) % 3 == 0:
            a = [sorted(p) for p in a]
        if len(calls) % 3 == 1:
            a = [sorted(p, reverse=True) for p in a]
        add(transactions=a)
    return list(calls)[:600]
