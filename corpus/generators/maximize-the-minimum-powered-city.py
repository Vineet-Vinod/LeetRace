import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, r, k = data["stations"], data["r"], data["k"]
        assert (
            1 <= len(a) <= 100000
            and all(0 <= x <= 100000 for x in a)
            and 0 <= r < len(a)
            and 0 <= k <= 1000000000
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"stations": [1, 2, 4, 5, 0], "r": 1, "k": 2},
        {"stations": [4, 4, 4, 4], "r": 0, "k": 3},
    ]:
        add(**example)
    add(stations=[0] * 100000, r=0, k=1000000000)
    add(stations=[100000] * 100000, r=99999, k=1000000000)
    add(stations=[0] * 100000, r=50000, k=0)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        a = [rng.randint(0, 100000 if len(calls) % 3 == 0 else 20) for _ in range(n)]
        add(
            stations=a,
            r=rng.choice([0, n - 1, rng.randrange(n)]),
            k=rng.choice([0, 1000000000, rng.randint(1, 1000)]),
        )
    assert len(calls) == 600
    return calls
