import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        assert 1 <= len(kw["arr"]) <= 100 and all(1 <= x <= 20 for x in kw["arr"])
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"arr": [1, 2]}, {"arr": [1, 3, 4, 1, 5]}] + [
        {"arr": [20] * 100},
        {"arr": list(range(1, 21)) * 5},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 20)
        v = [rng.randint(1, 5) for _ in range(n)]
        if len(calls) % 3 == 0:
            v = v + v[::-1]
        if len(calls) % 3 == 1:
            v = [rng.randint(1, 20) for _ in range(n)]
        add(arr=v)
    return calls
