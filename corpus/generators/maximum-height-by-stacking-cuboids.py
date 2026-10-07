import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(cuboids: list[list[int]]) -> None:
        assert 1 <= len(cuboids) <= 100 and all(
            len(c) == 3 and all(1 <= v <= 100 for v in c) for c in cuboids
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("cuboids", cuboids)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(cuboids=[[50, 45, 20], [95, 37, 53], [45, 23, 12]])
    add(cuboids=[[100, 100, 100]] * 100)
    add(cuboids=[[i, i, i] for i in range(1, 101)])
    add(cuboids=[[50, 45, 20], [95, 37, 53], [45, 23, 12]])
    add(cuboids=[[38, 25, 45], [76, 35, 3]])
    add(
        cuboids=[
            [7, 11, 17],
            [7, 17, 11],
            [11, 7, 17],
            [11, 17, 7],
            [17, 7, 11],
            [17, 11, 7],
        ]
    )
    while len(calls) < 600:
        n = rng.randint(1, 25)
        cuboids = [[rng.randint(1, 100) for _ in range(3)] for _ in range(n)]
        if len(calls) % 4 == 0:
            c = [rng.randint(1, 100) for _ in range(3)]
            cuboids = [c[:]] * n
        add(cuboids=cuboids)
    return calls
