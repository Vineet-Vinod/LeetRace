import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["nums"]
        assert 1 <= len(a) <= 100000 and all(1 <= v <= 30 for v in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums=[1, 2, 3, 4])
    add(nums=[4, 2, 3, 15])
    add(nums=[1] * 99999 + [30])
    add(nums=[30] * 100000)
    add(nums=[1] * 100000)
    add(nums=[1, 2, 3, 4])
    add(nums=[4, 2, 3, 15])
    while len(calls) < 600:
        n = rng.randint(1, 50)
        if len(calls) % 3 == 0:
            a = rng.choices([1, 4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28], k=n)
        elif len(calls) % 3 == 1:
            a = rng.choices([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 30], k=n)
        else:
            a = [rng.randint(1, 30) for _ in range(n)]
        add(nums=a)
    return list(calls)[:600]
