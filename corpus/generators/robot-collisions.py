import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        p, h, d = kw["positions"], kw["healths"], kw["directions"]
        assert 1 <= len(p) == len(h) == len(d) <= 100000 and len(set(p)) == len(p)
        assert all(1 <= x <= 10**9 for x in p + h) and set(d) <= set("LR")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {
            "positions": [5, 4, 3, 2, 1],
            "healths": [2, 17, 9, 15, 10],
            "directions": "RRRRR",
        },
        {"positions": [3, 5, 2, 6], "healths": [10, 10, 15, 12], "directions": "RLRL"},
        {"positions": [1, 2, 5, 6], "healths": [10, 10, 11, 11], "directions": "RLRL"},
    ] + [
        {
            "positions": list(range(1, 100001)),
            "healths": [10**9] * 100000,
            "directions": "RL" * 50000,
        },
        {
            "positions": list(range(100000, 0, -1)),
            "healths": [1] * 100000,
            "directions": "L" * 100000,
        },
        {"positions": [10**9], "healths": [10**9], "directions": "R"},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        p = rng.sample(range(1, 10000), n)
        h = [rng.randint(1, 15) for _ in p]
        d = "".join(rng.choice("LR") for _ in p)
        if len(calls) % 5 == 0:
            d = "R" * n
        if len(calls) % 5 == 1:
            h = [rng.randint(1, 15)] * n
            directions = {
                pos: ("R" if i % 2 == 0 else "L") for i, pos in enumerate(sorted(p))
            }
            d = "".join(directions[pos] for pos in p)
        add(positions=p, healths=h, directions=d)
    return calls
