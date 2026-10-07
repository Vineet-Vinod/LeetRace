import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        v = kw["target"]
        assert 1 <= len(v) <= 100000 and all(1 <= x <= 100000 for x in v)
        assert v[0] + sum(max(0, b - a) for a, b in zip(v, v[1:])) <= 2**31 - 1
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"target": [1, 2, 3, 2, 1]},
        {"target": [3, 1, 1, 2]},
        {"target": [3, 1, 5, 4, 2]},
    ] + [
        {"target": [100000] * 100000},
        {"target": [1, 40000] * 50000},
        {"target": [1]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        v = [rng.randint(1, 100000) for _ in range(n)]
        if len(calls) % 4 == 0:
            v = sorted(v)
        if len(calls) % 4 == 1:
            v = sorted(v, reverse=True)
        if len(calls) % 4 == 2:
            v = [rng.randint(1, 100000)] * n
        add(target=v)
    return calls
