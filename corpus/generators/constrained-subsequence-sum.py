import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, k = data["nums"], data["k"]
        assert 1 <= k <= len(a) <= 100000 and all(-10000 <= x <= 10000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"nums": [10, 2, -10, 5, 20], "k": 2},
        {"nums": [-1, -2, -3], "k": 1},
        {"nums": [10, -2, -10, -5, 20], "k": 2},
    ]:
        add(**example)
    add(nums=[10000] * 100000, k=100000)
    add(nums=[-10000] * 100000, k=1)
    add(nums=[10000, -10000] * 50000, k=2)
    while len(calls) < 600:
        n = rng.randint(1, 70)
        mode = len(calls) % 5
        a = [rng.randint(-10000, 10000) for _ in range(n)]
        if mode == 0:
            a = [-rng.randint(1, 10000) for _ in range(n)]
        if mode == 1:
            a = [rng.randint(0, 10000) for _ in range(n)]
        if mode == 2:
            a = [rng.choice([-10, 0, 10]) for _ in range(n)]
        add(nums=a, k=rng.choice([1, n, rng.randint(1, n)]))
    assert len(calls) == 600
    return calls
