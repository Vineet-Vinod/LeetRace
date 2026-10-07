import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["nums"]
        assert 1 <= len(a) <= 30 and all(0 <= v <= 10000 for v in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums=[1, 2, 3, 4, 5, 6, 7, 8])
    add(nums=[3, 1])
    add(nums=[10000] * 30)
    add(nums=[0] * 30)
    add(nums=[10000] + [0] * 29)
    add(nums=[rng.randint(0, 10000) for _ in range(30)])
    add(nums=[1, 2, 3, 4, 5, 6, 7, 8])
    add(nums=[3, 1])
    add(nums=[0])
    while len(calls) < 600:
        mode = len(calls) % 3
        if mode == 0:
            half = [rng.randint(0, 10000) for _ in range(rng.randint(1, 10))]
            a = half + half
            rng.shuffle(a)
        elif mode == 1:
            a = rng.sample(range(10001), 2)
        else:
            a = [rng.randint(0, 50) for _ in range(rng.randint(1, 16))]
        add(nums=a)
    return list(calls)[:600]
