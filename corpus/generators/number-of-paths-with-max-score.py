import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        g = kwargs["board"]
        n = len(g)
        assert 2 <= n <= 100 and all(len(row) == n for row in g)
        assert g[0][0] == "E" and g[-1][-1] == "S"
        assert all(
            c in "123456789X"
            for i, row in enumerate(g)
            for j, c in enumerate(row)
            if (i, j) not in [(0, 0), (n - 1, n - 1)]
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(board=["E23", "2X2", "12S"])
    add(board=["E12", "1X1", "21S"])
    add(board=["E11", "XXX", "11S"])
    add(board=["E" + "9" * 99] + ["9" * 100] * 98 + ["9" * 99 + "S"])
    add(board=["E" + "1" * 99] + ["X" * 100] + ["1" * 100] * 97 + ["1" * 99 + "S"])
    while len(calls) < 600:
        n = rng.randint(2, 12)
        g = [
            rng.choices("123456789X", weights=[1] * 9 + [rng.randint(0, 8)], k=n)
            for _ in range(n)
        ]
        g[0][0] = "E"
        g[-1][-1] = "S"
        add(board=["".join(row) for row in g])
    return calls
