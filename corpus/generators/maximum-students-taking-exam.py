import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        g = kwargs["seats"]
        assert 1 <= len(g) <= 8 and 1 <= len(g[0]) <= 8
        assert all(len(row) == len(g[0]) and set(row) <= set(".#") for row in g)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        seats=[
            ["#", ".", "#", "#", ".", "#"],
            [".", "#", "#", "#", "#", "."],
            ["#", ".", "#", "#", ".", "#"],
        ]
    )
    add(seats=[[".", "#"], ["#", "#"], ["#", "."], ["#", "#"], [".", "#"]])
    add(
        seats=[
            ["#", ".", ".", ".", "#"],
            [".", "#", ".", "#", "."],
            [".", ".", "#", ".", "."],
            [".", "#", ".", "#", "."],
            ["#", ".", ".", ".", "#"],
        ]
    )
    add(seats=[list("." * 8) for _ in range(8)])
    add(seats=[list("#" * 8) for _ in range(8)])
    add(seats=[["."]])
    add(seats=[["#"]])
    while len(calls) < 600:
        m, n = rng.randint(1, 8), rng.randint(1, 8)
        g = [
            rng.choices(".#", weights=[rng.randint(1, 8), rng.randint(1, 8)], k=n)
            for _ in range(m)
        ]
        add(seats=g)
    return calls
