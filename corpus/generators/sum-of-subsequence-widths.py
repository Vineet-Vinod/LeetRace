import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 1 <= len(kw["nums"]) <= 100000 and all(
            1 <= x <= 100000 for x in kw["nums"]
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"nums": [2, 1, 3]}, {"nums": [2]}] + [
        {"nums": list(range(1, 100001))},
        {"nums": [100000] * 100000},
        {"nums": [1, 100000] * 50000},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        v = [rng.randint(1, 100000) for _ in range(n)]
        if len(calls) % 4 == 0:
            v = [rng.randint(1, 100000)] * n
        if len(calls) % 4 == 1:
            v = [rng.randint(1, 10) for _ in range(n)]
        add(nums=v)
    return calls
