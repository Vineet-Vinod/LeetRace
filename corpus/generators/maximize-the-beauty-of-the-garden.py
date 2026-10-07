import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["flowers"]
        assert 2 <= len(a) <= 100000 and all(-10000 <= x <= 10000 for x in a)
        assert len(set(a)) < len(a)  # Duplicate endpoints prove a valid garden exists.
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(flowers=[1, 2, 3, 1, 2])
    add(flowers=[100, 1, 1, -3, 1])
    add(flowers=[-1, -2, 0, -1])
    add(flowers=[10000] * 100000)
    add(flowers=[-10000] * 100000)
    add(flowers=[1, 2, 3, 1, 2])
    add(flowers=[100, 1, 1, -3, 1])
    add(flowers=[-1, -2, 0, -1])
    while len(calls) < 600:
        n = rng.randint(2, 65)
        a = [rng.randint(-100, 100) for _ in range(n)]
        if len(calls) % 3 == 0:
            a = [-rng.randint(1, 100) for _ in range(n)]
        a[-1] = a[rng.randrange(n - 1)]
        add(flowers=a)
    return list(calls)[:600]
