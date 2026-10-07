import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        rectangles = values["rectangles"]
        assert 1 <= len(rectangles) <= 20000 and all(
            len(r) == 4
            and -100000 <= r[0] < r[2] <= 100000
            and -100000 <= r[1] < r[3] <= 100000
            for r in rectangles
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(rectangles=[[-100000, -100000, 100000, 100000]])
    emit(rectangles=[[i, 0, i + 1, 1] for i in range(20000)])
    emit(rectangles=[[0, 0, 1, 1], [0, 0, 1, 1]])
    while len(calls) < 600:
        x, y = rng.randint(-100, 100), rng.randint(-100, 100)
        m, n = rng.randint(1, 8), rng.randint(1, 8)
        rectangles = [
            [x + i, y + j, x + i + 1, y + j + 1] for i in range(m) for j in range(n)
        ]
        mode = len(calls) % 3
        if mode == 1:
            rectangles.append(rng.choice(rectangles).copy())
        elif mode == 2 and len(rectangles) > 2:
            rectangles.pop(rng.randrange(len(rectangles)))
        rng.shuffle(rectangles)
        emit(rectangles=rectangles)
    return calls
