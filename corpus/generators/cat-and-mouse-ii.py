import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        assert (
            1 <= len(g) <= 8
            and 1 <= len(g[0]) <= 8
            and all(len(row) == len(g[0]) for row in g)
        )
        s = "".join(g)
        assert set(s) <= set("CMF.#") and all(s.count(c) == 1 for c in "CMF")
        assert 1 <= d["catJump"] <= 8 and 1 <= d["mouseJump"] <= 8

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=["####F", "#C...", "M...."], catJump=1, mouseJump=2)
    add(grid=["M.C...F"], catJump=1, mouseJump=4)
    add(grid=["M.C...F"], catJump=1, mouseJump=3)
    for cj, mj in ((1, 1), (1, 8), (8, 1), (8, 8)):
        add(
            grid=["M......F"] + ["........"] * 6 + ["C......."],
            catJump=cj,
            mouseJump=mj,
        )
    add(grid=["M#F#C"], catJump=8, mouseJump=8)
    t = 0
    while len(calls) < 600:
        rows, cols = rng.randint(1, 4), rng.randint(1, 5)
        if rows * cols < 3:
            rows = 3
        cells = ["#" if rng.random() < 0.3 else "." for _ in range(rows * cols)]
        for index, char in zip(rng.sample(range(rows * cols), 3), "MCF"):
            cells[index] = char
        add(
            grid=["".join(cells[i * cols : (i + 1) * cols]) for i in range(rows)],
            catJump=rng.randint(1, 8),
            mouseJump=rng.randint(1, 8),
        )
        t += 1
    return calls
