import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(obstacles):
        assert 1 <= len(obstacles) <= 100000
        assert all(1 <= x <= 10000000 for x in obstacles)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}" for name, value in (("obstacles", obstacles),)
            )
            + ")"
        )
        calls[call] = None

    add(obstacles=[1, 2, 3, 2])
    add(obstacles=[2, 2, 1])
    add(obstacles=[3, 1, 5, 6, 4, 2])
    add(obstacles=list(range(1, 100001)))
    add(obstacles=[10000000] * 100000)
    add(obstacles=[1])
    while len(calls) < 600:
        n = rng.randint(1, 65)
        mode = rng.randrange(5)
        obstacles = [rng.randint(1, 15) for _ in range(n)]
        if mode == 0:
            obstacles.sort()
        elif mode == 1:
            obstacles.sort(reverse=True)
        elif mode == 2:
            obstacles = [rng.randint(1, 10000000)] * n
        elif mode == 3:
            obstacles = [rng.choice((1, 10000000)) for _ in range(n)]
        add(obstacles=obstacles)
    return list(calls)
