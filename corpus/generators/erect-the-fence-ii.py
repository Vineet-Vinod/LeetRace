import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        trees = values["trees"]
        assert 1 <= len(trees) <= 3000 and all(
            len(p) == 2 and all(0 <= x <= 3000 for x in p) for p in trees
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for trees in (
        [[0, 0]],
        [[3000, 3000]],
        [[0, 0], [3000, 3000]],
        [[1, 2], [2, 2], [4, 2]],
        [[0, 0], [3000, 0], [1500, 3000]],
        [[i, 0] for i in range(3000)],
    ):
        emit(trees=trees)
    while len(calls) < 600:
        n = rng.randint(1, 20)
        mode = len(calls) % 4
        if mode == 0:
            y = rng.randint(0, 3000)
            trees = [[rng.randint(0, 3000), y] for _ in range(n)]
        else:
            trees = [[rng.randint(0, 3000), rng.randint(0, 3000)] for _ in range(n)]
        emit(trees=trees)
    return calls
