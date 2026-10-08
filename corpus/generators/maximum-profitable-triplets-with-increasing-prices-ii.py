import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a, b = args["prices"], args["profits"]
        assert 3 <= len(a) == len(b) <= 50000
        assert all(1 <= x <= 5000 for x in a) and all(1 <= x <= 1000000 for x in b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(prices=[10, 2, 3, 4], profits=[100, 2, 7, 10])
    add(prices=[1, 2, 3, 4, 5], profits=[1, 5, 3, 4, 6])
    add(prices=[4, 3, 2, 1], profits=[33, 20, 19, 87])
    add(prices=[1, 2, 5000] * 16666 + [1, 5000], profits=[1000000] * 50000)
    add(prices=[5000] * 50000, profits=[1] * 50000)
    add(prices=[10, 2, 3, 4], profits=[100, 2, 7, 10])
    while len(calls) < 600:
        n = rng.randint(3, 55)
        a = [rng.randint(1, 50) for _ in range(n)]
        if len(calls) % 3 == 0:
            a.sort()
        if len(calls) % 3 == 1:
            a.sort(reverse=True)
        add(prices=a, profits=[rng.randint(1, 1000000) for _ in range(n)])
    return list(calls)[:600]
