import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 2 <= kw["x"] <= 100 and 1 <= kw["target"] <= 2 * 10**8
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"x": 3, "target": 19},
        {"x": 5, "target": 501},
        {"x": 100, "target": 100000000},
    ] + [
        {"x": 2, "target": 200000000},
        {"x": 100, "target": 1},
        {"x": 2, "target": 1},
        {"x": 100, "target": 200000000},
    ]:
        add(**kw)
    while len(calls) < 600:
        x = rng.randint(2, 100)
        if len(calls) % 3 == 0:
            power = x ** rng.randint(0, 7)
            target = max(1, min(2 * 10**8, power + rng.choice([-1, 0, 1])))
        else:
            target = rng.randint(1, 2 * 10**8)
        add(x=x, target=target)
    return calls
