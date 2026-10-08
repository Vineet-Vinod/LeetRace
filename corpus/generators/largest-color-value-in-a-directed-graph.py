import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(colors, edges):
        n = len(colors)
        assert 1 <= n <= 100000 and set(colors) <= set("abcdefghijklmnopqrstuvwxyz")
        assert len(edges) <= 100000 and all(0 <= a < n and 0 <= b < n for a, b in edges)

    add(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]])
    add(colors="a", edges=[[0, 0]])
    while len(calls) < 598:
        n = rng.randint(1, 30)
        colors = "".join(rng.choices("abcd", k=n))
        mode = len(calls) % 3
        edges = [
            [a, b] for a in range(n) for b in range(a + 1, n) if rng.random() < 0.13
        ]
        if mode == 1:
            edges.append([rng.randrange(n)] * 2)
        if mode == 2 and n > 1:
            edges += [[i, i + 1] for i in range(n - 1)] + [[n - 1, 0]]
        add(colors=colors, edges=edges)
    calls['candidate(colors="a"*100000, edges=[[i,i+1] for i in range(99999)])'] = None
    calls['candidate(colors="z"*100000, edges=[[i,i] for i in range(100000)])'] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
