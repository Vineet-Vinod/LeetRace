import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        w, h, side_length, m = (
            kw["width"],
            kw["height"],
            kw["sideLength"],
            kw["maxOnes"],
        )
        assert (
            1 <= w <= 100
            and 1 <= h <= 100
            and 1 <= side_length <= min(w, h)
            and 0 <= m <= side_length * side_length
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"width": 3, "height": 3, "sideLength": 2, "maxOnes": 1},
        {"width": 3, "height": 3, "sideLength": 2, "maxOnes": 2},
    ] + [
        {"width": 100, "height": 100, "sideLength": 100, "maxOnes": 10000},
        {"width": 100, "height": 100, "sideLength": 1, "maxOnes": 1},
        {"width": 1, "height": 1, "sideLength": 1, "maxOnes": 0},
    ]:
        add(**kw)
    while len(calls) < 600:
        w, h = rng.randint(1, 100), rng.randint(1, 100)
        side_length = rng.randint(1, min(w, h))
        m = rng.randint(0, side_length * side_length)
        if len(calls) % 6 == 0:
            m = 0
        if len(calls) % 6 == 1:
            m = side_length * side_length
        add(width=w, height=h, sideLength=side_length, maxOnes=m)
    return calls
