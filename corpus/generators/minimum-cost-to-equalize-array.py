import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a = args["nums"]
        assert 1 <= len(a) <= 100000 and all(1 <= x <= 1000000 for x in a)
        assert 1 <= args["cost1"] <= 1000000 and 1 <= args["cost2"] <= 1000000
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums=[1, 1000000, 1000000], cost1=1000000, cost2=1000000)
    add(nums=[4, 1], cost1=5, cost2=2)
    add(nums=[2, 3, 3, 3, 5], cost1=2, cost2=1)
    add(nums=[3, 5, 3], cost1=1, cost2=3)
    add(nums=[1] * 99999 + [1000000], cost1=1000000, cost2=1)
    add(nums=[1, 1000000, 1000000], cost1=1000000, cost2=1)
    add(nums=[1000000], cost1=1000000, cost2=1000000)
    add(nums=[4, 1], cost1=5, cost2=2)
    add(nums=[2, 3, 3, 3, 5], cost1=2, cost2=1)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        a = [rng.randint(1, 100) for _ in range(n)]
        if len(calls) % 4 == 0:
            a = [rng.randint(1, 100)] * n
        add(nums=a, cost1=rng.randint(1, 1000), cost2=rng.randint(1, 1000))
    return list(calls)[:600]
