import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        assert 0 <= args["k"] <= 10**9
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(k=0)
    add(k=1)
    add(k=0)
    add(k=1)
    add(k=10**9)
    for jumps in range(30):
        for down in range(jumps + 2):
            k = 2**jumps - down
            if 0 <= k <= 10**9:
                add(k=k)
    while len(calls) < 600:
        add(k=rng.randint(0, 10**9))
    return list(calls)[:600]
