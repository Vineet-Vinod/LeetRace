import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        p = args["paint"]
        assert 1 <= len(p) <= 100000
        assert all(
            len(interval) == 2 and 0 <= interval[0] < interval[1] <= 50000
            for interval in p
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(paint=[[1, 4], [4, 7], [5, 8]])
    add(paint=[[1, 4], [5, 8], [4, 7]])
    add(paint=[[1, 5], [2, 4]])
    add(paint=[[1, 4], [4, 7], [5, 8]])
    add(paint=[[0, 50000]] * 100000)
    add(paint=[[i, i + 1] for i in range(50000)])
    add(paint=[[0, 1]])
    while len(calls) < 600:
        n = rng.randint(1, 45)
        if len(calls) % 3 == 0:
            p = [[0, rng.randint(1, 50)] for _ in range(n)]
        else:
            p = [sorted(rng.sample(range(101), 2)) for _ in range(n)]
        add(paint=p)
    return list(calls)[:600]
