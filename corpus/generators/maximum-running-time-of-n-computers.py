import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, n = data["batteries"], data["n"]
        assert 1 <= n <= len(a) <= 100000 and all(1 <= x <= 1000000000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"n": 2, "batteries": [3, 3, 3]},
        {"n": 2, "batteries": [1, 1, 1, 1]},
    ]:
        add(**example)
    add(n=100000, batteries=[1000000000] * 100000)
    add(n=1, batteries=[1000000000] * 100000)
    add(n=99999, batteries=[1] * 99999 + [1000000000])
    while len(calls) < 600:
        length = rng.randint(1, 80)
        mode = len(calls) % 3
        a = [rng.randint(1, 1000000000 if mode == 0 else 100) for _ in range(length)]
        if mode == 1:
            a[0] = 1000000000
        add(n=rng.choice([1, length, rng.randint(1, length)]), batteries=a)
    assert len(calls) == 600
    return calls
