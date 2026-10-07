import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["ratings"]
        assert 1 <= len(a) <= 20000 and all(0 <= x <= 20000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(ratings=[1, 0, 2])
    add(ratings=[1, 2, 2])
    add(ratings=list(range(20000)))
    add(ratings=list(range(20000, 0, -1)))
    add(ratings=[20000] * 20000)
    add(ratings=[1, 0, 2])
    add(ratings=[1, 2, 2])
    add(ratings=[0])
    while len(calls) < 600:
        n = rng.randint(1, 65)
        a = [rng.randint(0, 20) for _ in range(n)]
        if len(calls) % 4 == 0:
            a.sort()
        if len(calls) % 4 == 1:
            a.sort(reverse=True)
        add(ratings=a)
    return list(calls)[:600]
