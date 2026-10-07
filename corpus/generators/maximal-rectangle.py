import random
from itertools import product


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    for x in ("0", "1"):
        add(matrix=[[x] * 200 for _ in range(200)])
    for bits in product("01", repeat=4):
        add(matrix=[list(bits[:2]), list(bits[2:])])
    while len(calls) < 600:
        m, n = rng.randint(1, 15), rng.randint(1, 15)
        density = rng.choice((0.15, 0.5, 0.85))
        matrix = [
            ["1" if rng.random() < density else "0" for _ in range(n)] for _ in range(m)
        ]
        assert (
            1 <= m <= 200
            and 1 <= n <= 200
            and all(x in "01" for row in matrix for x in row)
        )
        add(matrix=matrix)
    assert len(calls) == 600
    return list(calls)
