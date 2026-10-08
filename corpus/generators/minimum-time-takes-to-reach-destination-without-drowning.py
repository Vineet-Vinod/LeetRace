import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    land = [["."] * 100 for _ in range(100)]
    land[0][0] = "S"
    land[-1][-1] = "D"
    add(land=land)
    land = [["X"] * 100 for _ in range(100)]
    land[0][0] = "S"
    land[-1][-1] = "D"
    add(land=land)
    while len(calls) < 600:
        m, n = rng.randint(2, 12), rng.randint(2, 12)
        alphabet = "...X*" if len(calls) % 2 else "....X"
        land = [[rng.choice(alphabet) for _ in range(n)] for _ in range(m)]
        s, d = rng.sample(range(m * n), 2)
        land[s // n][s % n] = "S"
        land[d // n][d % n] = "D"
        assert (
            sum(row.count("S") for row in land)
            == sum(row.count("D") for row in land)
            == 1
        )
        assert (
            2 <= m <= 100
            and 2 <= n <= 100
            and all(x in "SD.X*" for row in land for x in row)
        )
        add(land=land)
    assert len(calls) == 600
    return list(calls)
