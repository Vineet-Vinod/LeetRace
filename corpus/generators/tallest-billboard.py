import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(rods=[1000] * 5)
    add(rods=[250] * 20)
    for rods in ([1], [1, 2], [1, 2, 3, 6], [1, 2, 3, 4, 5, 6]):
        add(rods=rods)
    while len(calls) < 600:
        n = rng.randint(1, 16)
        if len(calls) % 3 == 0:
            # Duplicate two arbitrary multisets to force a positive achievable height.
            half = [rng.randint(1, 150) for _ in range(max(1, n // 2))]
            rods = half + half
            rng.shuffle(rods)
        else:
            rods = [rng.randint(1, 250) for _ in range(n)]
        assert (
            1 <= len(rods) <= 20
            and all(1 <= x <= 1000 for x in rods)
            and sum(rods) <= 5000
        )
        add(rods=rods)
    assert len(calls) == 600
    return list(calls)
