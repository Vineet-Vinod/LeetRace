import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        assert 1 <= args["n"] <= 5000
        assert len(args["rollMax"]) == 6 and all(1 <= x <= 15 for x in args["rollMax"])
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(n=2, rollMax=[1, 1, 2, 2, 2, 3])
    add(n=2, rollMax=[1, 1, 1, 1, 1, 1])
    add(n=3, rollMax=[1, 1, 1, 2, 2, 3])
    add(n=5000, rollMax=[15] * 6)
    add(n=5000, rollMax=[1] * 6)
    add(n=2, rollMax=[1, 1, 2, 2, 2, 3])
    add(n=3, rollMax=[1, 1, 1, 2, 2, 3])
    while len(calls) < 600:
        add(n=rng.randint(1, 70), rollMax=[rng.randint(1, 15) for _ in range(6)])
    return list(calls)[:600]
