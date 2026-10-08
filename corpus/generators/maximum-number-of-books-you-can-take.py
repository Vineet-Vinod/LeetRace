import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["books"]
        assert 1 <= len(a) <= 100000 and all(0 <= x <= 100000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(books=[8, 5, 2, 7, 9])
    add(books=[7, 0, 3, 4, 5])
    add(books=[8, 2, 3, 7, 3, 4, 0, 1, 4, 3])
    add(books=[100000] * 100000)
    add(books=[0] * 100000)
    add(books=list(range(1, 100001)))
    add(books=[8, 5, 2, 7, 9])
    add(books=[7, 0, 3, 4, 5])
    while len(calls) < 600:
        n = rng.randint(1, 65)
        a = [rng.randint(0, 100) for _ in range(n)]
        if len(calls) % 4 == 0:
            a.sort()
        if len(calls) % 4 == 1:
            a.sort(reverse=True)
        add(books=a)
    return list(calls)[:600]
