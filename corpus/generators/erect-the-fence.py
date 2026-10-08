import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        trees = kwargs["trees"]
        assert 1 <= len(trees) <= 3000 and len(set(map(tuple, trees))) == len(trees)
        assert all(len(p) == 2 and all(0 <= v <= 100 for v in p) for p in trees)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(trees=[[x, y] for x in range(30) for y in range(100)])
    add(trees=[[0, 0], [0, 100], [100, 0], [100, 100], [50, 0], [50, 50]])
    add(trees=[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
    add(trees=[[1, 2], [2, 2], [4, 2]])
    while len(calls) < 600:
        mode = len(calls) % 3
        pool = (
            [(x, y) for x in range(15) for y in range(15)]
            if mode
            else [(x, rng.randrange(101)) for x in range(101)]
        )
        trees = [list(p) for p in rng.sample(pool, rng.randint(1, min(45, len(pool))))]
        if mode == 1:
            trees = [[x, 50] for x in rng.sample(range(101), rng.randint(1, 40))]
        add(trees=trees)
    return calls
