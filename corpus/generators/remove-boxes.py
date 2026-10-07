import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(boxes):
        assert 1 <= len(boxes) <= 100 and all(1 <= v <= 100 for v in boxes)

    add(boxes=[1, 3, 2, 2, 2, 3, 4, 3, 1])
    while len(calls) < 596:
        n = rng.randint(1, 20)
        boxes = [rng.randint(1, rng.choice([2, 3, 5, 100])) for _ in range(n)]
        if len(calls) % 4 == 0:
            boxes = [rng.randint(1, 100)] * n
        add(boxes=boxes)
    calls["candidate(boxes=[1]*100)"] = None
    calls["candidate(boxes=list(range(1,101)))"] = None
    calls["candidate(boxes=[1,2]*50)"] = None
    calls["candidate(boxes=[1]*30+[2]*40+[1]*30)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
