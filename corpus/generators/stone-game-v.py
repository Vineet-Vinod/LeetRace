import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(stoneValue):
        assert 1 <= len(stoneValue) <= 500 and all(
            1 <= v <= 1000000 for v in stoneValue
        )
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}" for name, value in (("stoneValue", stoneValue),)
            )
            + ")"
        )
        calls[call] = None

    add(stoneValue=[6, 2, 3, 4, 5, 5])
    add(stoneValue=[7, 7, 7, 7, 7, 7, 7])
    add(stoneValue=[4])
    add(stoneValue=[1000000] * 500)
    add(stoneValue=list(range(1, 501)))
    add(stoneValue=[1])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        mode = rng.randrange(5)
        values = [rng.randint(1, 30) for _ in range(n)]
        if mode == 0:
            values = [rng.randint(1, 1000000)] * n
        elif mode == 1:
            values = [1000000] + [1] * (n - 1)
        elif mode == 2:
            values.sort()
        elif mode == 3:
            values.sort(reverse=True)
        add(stoneValue=values)
    return list(calls)
