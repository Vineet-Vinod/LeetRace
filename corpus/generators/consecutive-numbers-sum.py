import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        assert 1 <= args["n"] <= 10**9
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(n=5)
    add(n=9)
    add(n=15)
    for n in [1, 5, 9, 15, 10**9, 999999937, 2**29, 73513440]:
        add(n=n)
    for n in range(1, 201):
        add(n=n)
    while len(calls) < 600:
        n = rng.randint(1, 10**9)
        add(n=n)
    return list(calls)[:600]
