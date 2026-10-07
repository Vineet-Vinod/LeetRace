import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(row):
        n = len(row) // 2
        assert len(row) == 2 * n and 2 <= n <= 30 and n % 2 == 0
        assert sorted(row) == list(range(2 * n))
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("row", row),))
            + ")"
        )
        calls[call] = None

    add(row=[0, 2, 1, 3])
    add(row=[3, 2, 0, 1])
    add(row=list(range(60)))
    add(row=list(range(0, 60, 2)) + list(range(1, 60, 2)))
    while len(calls) < 600:
        n = 2 * rng.randint(1, 15)
        row = list(range(2 * n))
        if len(calls) % 4 == 0:
            pairs = [row[i : i + 2] for i in range(0, 2 * n, 2)]
            rng.shuffle(pairs)
            for pair in pairs:
                rng.shuffle(pair)
            row = [v for pair in pairs for v in pair]
        else:
            rng.shuffle(row)
        add(row=row)
    return list(calls)
