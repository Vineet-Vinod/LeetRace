import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["nums"]
        assert 1 <= len(a) <= 50000 and all(0 <= x <= 100000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"nums": [1, 4, 2, 5, 3]},
        {"nums": [3, 2, 1]},
        {"nums": [2, 2, 2]},
    ]:
        add(**example)
    add(nums=[0] * 50000)
    add(nums=list(range(50000)))
    add(nums=list(range(100000, 50000, -1)))
    while len(calls) < 600:
        a = [
            rng.randint(0, 100000 if len(calls) % 3 == 0 else 10)
            for _ in range(rng.randint(1, 80))
        ]
        if len(calls) % 4 == 0:
            a.sort()
        if len(calls) % 4 == 1:
            a.sort(reverse=True)
        add(nums=a)
    assert len(calls) == 600
    return calls
