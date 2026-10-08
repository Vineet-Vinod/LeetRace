import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["stones"]
        assert 2 <= len(a) <= 2000 and a[0] == 0 and all(0 <= x <= 2**31 - 1 for x in a)
        assert all(x < y for x, y in zip(a, a[1:]))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(stones=[0, 1, 3, 5, 6, 8, 12, 17])
    add(stones=[0, 1, 2, 3, 4, 8, 9, 11])
    add(stones=list(range(2000)))
    add(stones=[i * (i + 1) // 2 for i in range(2000)])
    add(stones=[0, 2**31 - 1])
    add(stones=[0, 1, 3, 5, 6, 8, 12, 17])
    add(stones=[0, 1, 2, 3, 4, 8, 9, 11])
    while len(calls) < 600:
        n = rng.randint(2, 55)
        a = [0]
        jump = 0
        if len(calls) % 2 == 0:
            # Following the legal jump rule constructs a reachable final stone.
            for _ in range(n - 1):
                jump = rng.choice([x for x in (jump - 1, jump, jump + 1) if x > 0])
                a.append(a[-1] + jump)
        else:
            a = [0] + sorted(rng.sample(range(2, 1000), n - 1))
        add(stones=a)
    return list(calls)[:600]
