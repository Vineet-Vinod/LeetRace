import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, k = data["nums"], data["k"]
        assert 1 <= k <= len(a) <= 100000 and all(1 <= x <= 1000000000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"nums": [2, 6, 5, 8], "k": 2}, {"nums": [4, 5, 4, 7], "k": 3}]:
        add(**example)
    add(nums=[1000000000] * 100000, k=100000)
    add(nums=[1] * 100000, k=1)
    add(nums=[1 << (i % 30) for i in range(100000)], k=50000)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        mode = len(calls) % 4
        a = [rng.randint(1, 1000000000 if mode == 0 else 255) for _ in range(n)]
        if mode == 1:
            a = [1 << rng.randrange(30) for _ in range(n)]
        if mode == 2:
            a = [rng.choice([1, 7, 15, 31, 1000000000]) for _ in range(n)]
        add(nums=a, k=rng.randint(1, n))
    assert len(calls) == 600
    return calls
