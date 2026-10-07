import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        rect = kwargs["rectangles"]
        assert 1 <= len(rect) <= 200 and all(
            len(r) == 4 and 0 <= r[0] < r[2] <= 10**9 and 0 <= r[1] < r[3] <= 10**9
            for r in rect
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(rectangles=[[0, 0, 10**9, 10**9]])
    add(rectangles=[[i, i, 10**9 - i, 10**9 - i] for i in range(200)])
    add(rectangles=[[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])
    add(rectangles=[[0, 0, 1000000000, 1000000000]])
    while len(calls) < 600:
        limit = rng.choice([10, 10**9])
        rectangles = []
        for _ in range(rng.randint(1, 18)):
            x1, x2 = sorted(rng.sample(range(limit + 1), 2))
            y1, y2 = sorted(rng.sample(range(limit + 1), 2))
            rectangles.append([x1, y1, x2, y2])
        add(rectangles=rectangles)
    return calls
