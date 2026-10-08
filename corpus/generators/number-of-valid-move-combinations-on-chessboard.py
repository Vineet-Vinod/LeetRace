import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        p, pos = args["pieces"], args["positions"]
        assert (
            1 <= len(p) == len(pos) <= 4
            and set(p) <= {"rook", "queen", "bishop"}
            and p.count("queen") <= 1
        )
        assert all(len(v) == 2 and all(1 <= x <= 8 for x in v) for v in pos)
        assert len(set(map(tuple, pos))) == len(pos)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(pieces=["rook"], positions=[[1, 1]])
    add(pieces=["queen"], positions=[[1, 1]])
    add(pieces=["bishop"], positions=[[4, 3]])
    for piece in ["rook", "queen", "bishop"]:
        for r in range(1, 9):
            for c in range(1, 9):
                add(pieces=[piece], positions=[[r, c]])
    for p, pos in [
        (["rook"] * 4, [[1, 1], [1, 8], [8, 1], [8, 8]]),
        (["queen", "bishop", "rook", "bishop"], [[4, 4], [4, 5], [5, 4], [5, 5]]),
        (["bishop"] * 4, [[1, 1], [1, 2], [8, 7], [8, 8]]),
        (["rook", "queen", "bishop"], [[1, 1], [1, 2], [2, 1]]),
    ]:
        add(pieces=p, positions=pos)
    while len(calls) < 600:
        n = 3 if len(calls) % 10 == 0 else 2
        p = [rng.choice(["rook", "bishop"]) for _ in range(n)]
        if len(calls) % 3 == 0:
            p[rng.randrange(n)] = "queen"
        pos = [[x // 8 + 1, x % 8 + 1] for x in rng.sample(range(64), n)]
        add(pieces=p, positions=pos)
    return list(calls)[:600]
