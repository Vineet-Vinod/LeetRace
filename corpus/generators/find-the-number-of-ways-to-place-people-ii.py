import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        p = kwargs["points"]
        assert 2 <= len(p) <= 1000
        assert all(len(x) == 2 and all(-(10**9) <= a <= 10**9 for a in x) for x in p)
        assert len(set(map(tuple, p))) == len(p)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(points=[[1, 1], [2, 2], [3, 3]])
    add(points=[[6, 2], [4, 4], [2, 6]])
    add(points=[[3, 1], [1, 3], [1, 1]])
    add(points=[[i, -i] for i in range(1000)])
    add(points=[[-(10**9), 10**9], [10**9, -(10**9)]])
    while len(calls) < 600:
        n = rng.randint(2, 28)
        mode = len(calls) % 4
        if mode == 0:
            p = [[i, i] for i in range(n)]
        elif mode == 1:
            p = [[i, -i] for i in range(n)]
        else:
            p = [
                list(x)
                for x in rng.sample(
                    [(i, j) for i in range(-7, 8) for j in range(-7, 8)], n
                )
            ]
        rng.shuffle(p)
        add(points=p)
    return calls
